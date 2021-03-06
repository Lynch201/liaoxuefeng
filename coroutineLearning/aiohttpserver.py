#!/usr/bin/python
# coding:utf-8
# 201609271714
# lynch.wang

import asyncio


from aiohttp import web


async def index():
	await asyncio.sleep(0.5)
	return web.Response(body=b'<h1>Index<h1>')


async def hello(request):
	await asyncio.sleep(0.5)
	text = '<h1>hello, %s!</h>' % request.match_info['name']
	return web.Response(body=text.encode('utf-8'))


async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	app.router.add_route('GET', '/hello/{name}', hello)
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
	print('Server started at http://127.0.0.1:8000...')
	return srv

try:
	loop = asyncio.get_event_loop()
	loop.run_until_complete(init(loop))
except OSError as e:
	print('except:', e)
	loop.close()
finally:
	loop.run_forever()

# we use browser to test our http server
# but if we want to di it by us, use urllib.request
# http.client is a more lower module
