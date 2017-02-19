import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from helpers import all_friends, birthdays
from helpers import get_parser


def notify_email():
    """Send birthday reminder email to all friends"""

    emails = [friend[2] for friend in all_friends()] + ['myemail@gmail.com']
    fromaddr = get_parser('GMAIL_CREDENTIALS', 'username')
    password = get_parser('GMAIL_CREDENTIALS', 'password')
    toaddr = emails

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(fromaddr, password)

    birthday_members = birthdays()
    for member in birthday_members:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = ", ".join(toaddr)
        msg['Subject'] = "CSE BIRTHDAY REMINDER"

        body = '''Hey, you guys, just a friendly reminder (super friendly, almost too friendly, really) that today is {}'s birthday.
        \nBirthdays come only once a year, so make sure to wish a birthday guy and have lots of fun!

        \nHappy Birthday {}

        \nRegards
        \n CSE'''.format(member[0], member[0])

        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
    server.quit()
