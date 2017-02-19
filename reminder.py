from send_email import notify_email
from send_hangout import notify_hangout
from send_sms import notify_sms


def main():
    notify_email()
    notify_hangout()
    notify_sms()


if __name__ == '__main__':
    main()
