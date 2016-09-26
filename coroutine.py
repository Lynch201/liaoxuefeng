#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def consumer():
    r = 'xyz'
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK -> '+str(n)

def produce(c):
    r = c.send(None)
    print(r)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
