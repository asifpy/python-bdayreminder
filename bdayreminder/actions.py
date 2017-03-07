
from bdayreminder.db.makedb import init_db
from bdayreminder.db.loader import sampledata, exceldata

from bdayreminder.services.emails import SendEmail
from bdayreminder.services.sms import SendSms
from bdayreminder.services.hangout import SendHangoutMessage

from bdayreminder.helpers import birthdays


syncdb = init_db
loadsampledata = sampledata
loadexceldata = exceldata


def runreminder(service):
    """Run reminder for the provided service"""

    services = {
        'email': SendEmail,
        'sms': SendSms,
        'hangout': SendHangoutMessage
    }

    birthday_members = birthdays()
    for member in birthday_members:
        services[service](member)()


def runallreminders():
    """Run all the reminders(email, sms and hangout)"""

    birthday_members = birthdays()
    for member in birthday_members:
        SendEmail(member)()  # send email
        SendHangoutMessage(member)()  # send hangout message
        SendSms(member)()  # send mobile sms


def runemailreminder():
    return runreminder('email')


def runsmsreminder():
    return runreminder('sms')


def runhangoutreminder():
    return runreminder('hangout')
