#!/usr/bin/python
# coding:utf-8
# 201609252252
# lynch.wang

from email.mime.text import MIMEText
msg = MIMEText('hello,send by python', 'plain', 'utf-8')

#from_addr = input('From:')
from_addr  = '1092376202@qq.com'
#password = input('Password: ')
password = 'gyctbpblynrdbada'

#to_addr = input('To: ')
to_addr = 'lynch201xdu@gmail.com'
#smtp_server = input('SMTP server: ')
smtp_server = 'smtp.gamil.com'


import smtplib
server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)

try:
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
except smtplib.SMTPAuthenticationError as e:
	#print(e)
	e_str = str(e)
	errordescription = e_str[5:len(e_str)-1]
	print(errordescription)
	# 就是想读出来那个bytes类型的字符串到底是个啥

finally:
	server.quit()
print('finish')
