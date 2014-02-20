import smtplib

username = "user@gmail.com"
password = "password"

vtext = "number@SmsGateway.com"
message = "SMS text message body goes here"

msg = """From: %s
To: %s
Subject: text-message
%s""" % (username, vtext, message)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(username,password)
server.sendmail(username, vtext, msg)
server.quit()






# #!/usr/bin/python
# 
# __author__ = """
# NAME: Abhijeet Rastogi (shadyabhi)
# Profile: http://www.google.com/profiles/abhijeet.1989
# """
# 
# import cookielib
# import urllib2
# from getpass import getpass
# import sys
# from urllib import urlencode
# from getopt import getopt
# 
# ask_username = True
# ask_password = True
# ask_message = True
# ask_number = True
# 
# def Usage():
#     print '\t-h, --help:  View help'
#     print '\t-u, --username: Username'
#     print '\t-p, --password: Password'
#     print '\t-n, --number: numbber to send the sms'
#     print '\t-m, --message: Message to send'
#     sys.exit(1)
# 
# 
# opts, args = getopt(sys.argv[1:], 'u:p:m:n:h',["username=","password=","message=","number=","help"])
# 
# for o,v in opts:
#     if o in ("-h", "--help"):
#         Usage()
#     elif o in ("-u", "--username"):
#         username = v
#         ask_username = False
#     elif o in ("-p", "--password"):
#         passwd = v
#         ask_password = False
#     elif o in ("-m", "--message"):
#         message = v
#         ask_message = False
#     elif o in ("-n", "--number"):
#         number = v
#         ask_number = False
# 
# #Credentials taken here
# if ask_username: username = raw_input("Enter USERNAME: ")
# if ask_password: passwd = getpass()
# if ask_message: message = raw_input("Enter Message: ")
# if ask_number: number = raw_input("Enter Mobile number: ")
# 
# #Logging into the SMS Site
# url = 'http://wwwg.way2sms.com//auth.cl'
# data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
# 
# #Remember, Cookies are to be handled
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# 
# # To fool way2sms as if a Web browser is visiting the site
# opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Ubuntu/9.10 (karmic) Firefox/3.5.3 GTB7.0')]
# usock = opener.open(url, data)
# try:
#     usock = opener.open(url, data)
# except IOError:
#     print "Check your internet connection"
#     sys.exit(1)
# 
# #urlencode performed.. Because it was done by the site as i checked through HTTP headers
# 
# message = urlencode({'message':message})
# message = message[message.find("=")+1:]
# 
# #SMS sending
# send_sms_url = 'http://wwwg.way2sms.com//FirstServletsms?custid='
# #Check this line with HTTP Headers, if script is not working
# send_sms_data = 'custid=undefined&HiddenAction=instantsms&Action=custfrom950000&login=&pass=&MobNo='+number+'&textArea='+message
# opener.addheaders = [('Referer','http://wwwg.way2sms.com//jsp/InstantSMS.jsp?val=0')]
# 
# try:
#     sms_sent_page = opener.open(send_sms_url,send_sms_data)
#     inp = open("log.html","w")
#     inp.write(sms_sent_page.read())
#     inp.close()
# 
# except IOError:
#     print "Check your internet connection( while sending sms)"
#     sys.exit(1)
# print "SMS sent!!!"