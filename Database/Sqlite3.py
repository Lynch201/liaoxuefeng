#!user/bin/python
# -*- coding: utf-8 -*-
# 201609260929
# lynch.wang

import os
import sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)

# 初始数据：
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 65)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")

cursor.close()
conn.commit()
conn.close()



def get_score_in(low, high):
	""" 返回指定分数区间的名字， 按分数从低到高排列 """
	conn = sqlite3.connect(db_file)
	cursor = conn.cursor()
	try:
		cursor.execute('select * from user where score between ? and ? order by score', (low, high))

		values = cursor.fetchall()
		#print(values)
	finally:
		cursor.close()
		conn.commit()
		conn.close()

	#print([x[1] for x in values])
	return [x[1] for x in values]

# get_score_in(0, 100)

# test
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('pass')
