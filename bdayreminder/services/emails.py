import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from bdayreminder.helpers import get_all_emails
from bdayreminder.services.base import BaseReminder


class SendEmail(BaseReminder):
    provider = 'GMAIL_CREDENTIALS'

    def __init__(self, bday_guy, *args, **kwargs):
        super(SendEmail, self).__init__(bday_guy, *args, **kwargs)

        self.email_body = self.env.get_template('email_body.html')
        self.email_subject = self.env.get_template('email_subject.html')
        self.toaddr = get_all_emails()

    def gmail_authenticate(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(self.username, self.password)
        return server

    def execute(self):
        server = self.gmail_authenticate()
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ", ".join(self.toaddr)
        msg['Subject'] = self.email_subject.render()
        body = self.email_body.render(bday_member=self.bday_guy.name)

        msg.attach(MIMEText(body, 'html'))
        text = msg.as_string()
        server.sendmail(self.username, self.toaddr, text)
        server.quit()
