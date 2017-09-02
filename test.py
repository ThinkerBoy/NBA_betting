import smtplib
from datetime import *

# AWS Config
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_USER = 'AKIAIIOQ6FO67TSJJMTQ'
EMAIL_HOST_PASSWORD = 'AumarJeWS50TzsSptU2pOLQ2QSXMQEDxiuE4M8a71XC4'
EMAIL_PORT = 587

me = "brian.sachtjen@gmail.com"
you = ("brian.sachtjen@gmail.com", "bws7vs@virginia.edu")
subject = "Game Lines " + datetime.strftime(datetime.today(), '%m-%d-%Y')
body = "please work"
msg  = "From: %s\r\nTo: %s\r\nSubject: %s\r\n%s\r\n\n" % (me, ", ".join(you), subject, body)

s = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
s.set_debuglevel(1)
s.starttls()
s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
s.sendmail(me, you, msg)
s.quit()