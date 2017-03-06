import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Environment, FileSystemLoader

from bdayreminder.helpers import (
    get_all_emails,
    get_parser
)


class SendEmail(object):
    def __init__(self, bday_guy, *args, **kwargs):
        self.fromaddr = get_parser('GMAIL_CREDENTIALS', 'username')
        self.password = get_parser('GMAIL_CREDENTIALS', 'password')

        env = self.jinja_env()
        self.email_body = env.get_template('email_body.html')
        self.email_subject = env.get_template('email_subject.html')

        self.toaddr = get_all_emails()
        self.bday_guy = bday_guy

    def __call__(self):
        self.execute()

    def jinja_env(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        templates_path = os.path.join(current_dir, 'templates')

        loader = FileSystemLoader(templates_path)
        return Environment(loader=loader)

    def gmail_authenticate(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(self.fromaddr, self.password)
        return server

    def execute(self):
        server = self.gmail_authenticate()
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = ", ".join(self.toaddr)
        msg['Subject'] = self.email_subject.render()
        body = self.email_body.render(bday_member=self.bday_guy.name)

        msg.attach(MIMEText(body, 'html'))
        text = msg.as_string()
        server.sendmail(self.fromaddr, self.toaddr, text)
        server.quit()
