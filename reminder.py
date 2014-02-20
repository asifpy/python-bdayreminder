import sqlite3
import datetime
import smtplib

conn=sqlite3.connect(':memory:',detect_types=sqlite3.PARSE_DECLTYPES) 
cur=conn.cursor()
#create table
cur.execute('CREATE TABLE friend(name TEXT, birth_date DATE)')
#insert friends information
cur.execute("insert into friend values(?, ?)", ('John', datetime.date(1985, 5, 19)))


cur.execute('select * from friend')

today = datetime.datetime.now()
for obj in cur.fetchall():
    if today.day == obj[1].day and today.month == obj[1].month:
        FROM = 'from@gmail.com'
        TO  = ['to@gmail.com']
        SUBJECT = "Birthday Reminder"
        TEXT = "Today {} is celebrating his/her birthday please whish him/her.".format(obj[0])

        # Prepare actual message
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
        username = 'username'
        password = 'password'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(FROM, TO, message)
        server.quit()
