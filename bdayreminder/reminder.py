from bdayreminder.services import (
    emails,
    hangout,
    sms
)
from bdayreminder.helpers import birthdays


if __name__ == '__main__':
    birthday_members = birthdays()

    for member in birthday_members:
        emails.SendEmail(member)()  # send email
        hangout.SendHangoutMessage(member)()  # send hangout message
        sms.SendSms(member)()  # send mobile sms
