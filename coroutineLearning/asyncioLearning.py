#!/usr/bin/python
# coding:utf-8
# 201609271132
# lynch.wang

import asyncio


@asyncio.coroutine
def hello():
	print("Hello World!")
	# 异步调用asyncio.sleep(1)
	r = yield from asyncio.sleep(1)
	print(r)

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行协程coroutine
loop.run_until_complete(hello())
loop.close()
