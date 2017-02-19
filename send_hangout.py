import sleekxmpp
from time import sleep

from helpers import all_friends, birthdays
from helpers import get_parser


class Jabber(sleekxmpp.ClientXMPP):
    def __init__(self, username, password, instance_name=None):
        jid = "%s/%s" % (username, instance_name) if instance_name else username
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
            from_account = "%s@%s" % (message['from'].user, message['from'].domain)

            if self.instance_name in message['body'].lower():
                message.reply("%s was listening!" % self.instance_name).send()
            else:
                pass


def notify_hangout():
    """Send hangout message to all friends"""

    birthday_members = birthdays()
    for member in birthday_members:
        message = "CSE BDAY REMINDER : Today is {}'s birthday, so make sure to wish a birthday guy and have lots of fun!. Happy birthday {}".format(member[0], member[0])
        emails = [friend[2] for friend in all_friends()] + ['saluasif@gmail.com']

        for email in emails:
            if '@gmail.com' in email:
                fromaddr = get_parser('GMAIL_CREDENTIALS', 'username')
                password = get_parser('GMAIL_CREDENTIALS', 'password')
                jabber = Jabber(fromaddr, password)
                jabber.send_msg(email, message)
                sleep(10)
                jabber.close()
