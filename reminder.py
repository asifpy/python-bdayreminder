from os.path import dirname, join
import sqlite3
import datetime
import cookielib
import urllib2
import os

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

path = lambda *ps: os.path.join(os.path.dirname(__file__), *ps)
localpath = lambda p: join(dirname(__file__), p)

conn = sqlite3.connect(
    localpath('friends.db'),
    detect_types=sqlite3.PARSE_DECLTYPES)
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
    emails = [friend[2] for friend in all_friends] + ['myemail@gmail.com']
    fromaddr = "myemail@gmail.com"
    toaddr = emails

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(fromaddr, "mypassword")

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


def send_sms(birthday_members):
    username = 'mynumber'
    passwd = 'mypassword'

    # Logging into the SMS Site
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

    # For Cookies:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # Adding Header detail:
    opener.addheaders = [
        ('User-Agent',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
    opener.open(url, data)

    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    opener.addheaders = [
        ('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]

    for member in birthday_members:
        message = "CSE BDAY REMINDER : Today {} is going to celebrate his birthday. Happy birthday {}".format(member[0], member[0])

        for friend in all_friends:
            if friend[3]:
                send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+friend[3]+'&message='+message+'&msgLen=136'
                opener.open(send_sms_url, send_sms_data)


def main():
    birthday_members = birthdays()
    send_email(birthday_members)
    send_sms(birthday_members)


if __name__ == '__main__':
    main()
