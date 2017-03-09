from http.cookiejar import CookieJar
import urllib.request

from bdayreminder.services.base import BaseReminder
from bdayreminder.helpers import get_all_mobiles


class SendSms(BaseReminder):
    provider = 'WAY2SMS_CREDENTIALS'

    def __init__(self, bday_guy, *args, **kwargs):
        super(SendSms, self).__init__(bday_guy, *args, **kwargs)

        self.sms_body = self.env.get_template('sms_body.txt')
        self.mobiles = get_all_mobiles()

    def execute(self):
        # Logging into the SMS Site
        url = 'http://site24.way2sms.com/Login1.action?'

        data = {
            'username': self.username,
            'password': self.password,
            'Submit': "Sign+in"
        }

        # For Cookies:
        cj = CookieJar()
        opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(cj)
        )

        # Adding Header detail:
        opener.addheaders = [
            ('User-Agent',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
        opener.open(url, urllib.parse.urlencode(data).encode("utf-8"))

        jession_id = str(cj).split('~')[1].split(' ')[0]
        referer = 'http://site25.way2sms.com/sendSMS?Token={}'.format(
            jession_id)
        opener.addheaders = [('Referer', referer)]

        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        message = self.sms_body.render(bday_member=self.bday_guy.name)

        for mobile in self.mobiles:
            send_sms_data = {
                'ssaction': 'ss',
                'Token': jession_id,
                'mobile': mobile,
                'message': message,
                'msgLen': 136
            }

            opener.open(
                send_sms_url,
                urllib.parse.urlencode(send_sms_data).encode("utf-8")
            )
