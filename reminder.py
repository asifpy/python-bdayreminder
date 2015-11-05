
from os.path import dirname, join
import os
import sqlite3
import datetime

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

path = lambda *ps: os.path.join(os.path.dirname(__file__), *ps)
localpath = lambda p: join(dirname(__file__), p)

conn = sqlite3.connect(localpath('friends.db'), detect_types=sqlite3.PARSE_DECLTYPES)
c = conn.cursor()
c.execute('select * from friend')
all_friends = c.fetchall()

def birthdays():
    bmembers = []
    today = datetime.datetime.now()

    for friend in all_friends:
        if today.day == friend[1].day and today.month == friend[1].month:
            bmembers.append(friend)
    return bmembers


def send_email(birthday_members):
    emails = [friend[2] for friend in all_friends]
    fromaddr = "myemail@gmail.com"
    toaddr = emails
    print toaddr

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

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(fromaddr, "Password")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()


def main():
    birthday_members = birthdays()
    send_email(birthday_members)


if __name__ == '__main__':
    main()

