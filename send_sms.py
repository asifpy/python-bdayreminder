import cookielib
import urllib2

from helpers import all_friends, birthdays
from helpers import get_parser


def notify_sms():
    """
    - Uses way2sms free API to send SMS
    - Sends SMS to all friends
    """
    birthday_members = birthdays()
    username = get_parser('WAY2SMS_CREDENTIALS', 'username')
    passwd = get_parser('WAY2SMS_CREDENTIALS', 'password')

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

        friends = all_friends()
        for friend in friends:
            if friend[3]:
                send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+friend[3]+'&message='+message+'&msgLen=136'
                opener.open(send_sms_url, send_sms_data)
