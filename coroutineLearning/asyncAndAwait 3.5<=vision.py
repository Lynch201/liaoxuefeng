#!/usr/bin/python
# coding:utf-8
# 201609271654
# lynch.wang

import asyncio


async def wget(host):
	print('wget %s...' % host)
	connect = asyncio.open_connection(host, 80)
	reader, writer = await connect
	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	await writer.drain()
	while True:
		line = await reader.readline()
		if line == b'\r\n':
			break
		print('(host %s) header > %s' % (host, line.decode('utf-8').rstrip()))
	writer.close()

loop = asyncio.get_event_loop()
task = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(task))
loop.close()
