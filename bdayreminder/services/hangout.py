import sleekxmpp
import os
from time import sleep

from jinja2 import Environment, FileSystemLoader

from bdayreminder.helpers import (
    get_all_emails,
    get_parser,
)


class Jabber(sleekxmpp.ClientXMPP):
    def __init__(self, username, password, instance_name=None):

        jid = "{}/{}".format(
            username,
            instance_name
        ) if instance_name else username

        super(Jabber, self).__init__(jid, password)

        self.instance_name = instance_name
        self.add_event_handler(
            'session_start',
            self.start,
            threaded=False,
            disposable=True
        )
        self.add_event_handler(
            'message',
            self.receive,
            threaded=True,
            disposable=False
        )

        if self.connect(('talk.google.com', '5222')):
            self.process(block=False)
        else:
            raise Exception("Unable to connect to Google Jabber server")

    def __del__(self):
        self.close()

    def close(self):
        self.disconnect(wait=False)

    def start(self, event):
        self.send_presence()
        self.get_roster()

    def send_msg(self, recipient, body):
        message = self.Message()
        message['to'] = recipient
        message['type'] = 'chat'
        message['body'] = body
        message.send()

    def receive(self, message):
        if message['type'] in ('chat', 'normal'):
            if self.instance_name in message['body'].lower():
                message.reply("%s was listening!" % self.instance_name).send()
            else:
                pass


class SendHangoutMessage(object):
    def __init__(self, bday_guy, *args, **kwargs):
        self.fromaddr = get_parser('GMAIL_CREDENTIALS', 'username')
        self.password = get_parser('GMAIL_CREDENTIALS', 'password')

        env = self.jinja_env()
        self.message = env.get_template('hangout_message.txt')

        self.toaddr = get_all_emails()
        self.bday_guy = bday_guy

    def __call__(self):
        self.execute()

    def jinja_env(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        templates_path = os.path.join(current_dir, 'templates')

        loader = FileSystemLoader(templates_path)
        return Environment(loader=loader)

    def execute(self):
        message = self.message.render(bday_member=self.bday_guy.name)

        for email in self.toaddr:
            if '@gmail.com' in email:
                jabber = Jabber(self.fromaddr, self.password)
                jabber.send_msg(email, message)
                sleep(10)
                jabber.close()
