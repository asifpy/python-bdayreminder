import os
import datetime
from sqlalchemy import extract
from configparser import ConfigParser

from bdayreminder.db.base import DBSession
from bdayreminder.db.models import Person


def birthdays():
    today = datetime.datetime.now()
    session = DBSession()

    bday_members = session.query(Person).filter(
        extract('day', Person.dob) == today.day).filter(
        extract('month', Person.dob) == today.month).all()
    session.close()
    return bday_members


def get_all_emails():
    session = DBSession()
    emails = session.query(Person.email).distinct().all()
    session.close()
    emails = [email[0] for email in emails]
    return emails


def get_all_mobiles():
    session = DBSession()
    mobiles = session.query(Person.mobile).distinct().all()
    session.close()
    mobiles = [mobile[0] for mobile in mobiles]
    return mobiles


def get_parser(section, name):
    parser = ConfigParser()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(current_dir, 'config.ini')
    parser.read(config_path)
    return parser.get(section, name)
