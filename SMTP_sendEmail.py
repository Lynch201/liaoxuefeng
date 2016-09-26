#!/usr/bin/python
# coding:utf-8
# 201609252252
# lynch.wang

from email.mime.text import MIMEText
msg = MIMEText('hello,send by python', 'plain', 'utf-8')

#from_addr = input('From:')
from_addr  = 'lynch201xdu@gamil.com'
#password = input('Password: ')
password = 'gg2937w9'

#to_addr = input('To: ')
to_addr = '1092376202@qq.com'
#smtp_server = input('SMTP server: ')
smtp_server = 'smtp.qq.com'


import smtplib
# the smtp_port for qqmail is 465 and need smtp.SMTP_SSL()
# and gmail is 587
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.set_debuglevel(1)

try:
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
except smtplib.SMTPAuthenticationError as e:
	print(e)
	errorCode, explaning = e
	print(explaning.decode('utf-8'))
	# 就是想读出来那个bytes类型的字符串到底是个啥
finally:
	server.quit()
print('finish')
