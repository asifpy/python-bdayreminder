import sqlite3
from os.path import dirname, join
import datetime

from ConfigParser import SafeConfigParser

localpath = lambda p: join(dirname(__file__), p)


def all_friends():
    conn = sqlite3.connect(
        localpath('friends.db'),
        detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    c.execute('select * from friend')
    return c.fetchall()


def get_parser(section, name):
    parser = SafeConfigParser()
    parser.read('credentials.INI')
    return parser.get(section, name)


def birthdays():
    bmembers = []
    today = datetime.datetime.now()

    for friend in all_friends:
        if today.day == friend[1].day and today.month == friend[1].month:
            bmembers.append(friend)
    return bmembers
