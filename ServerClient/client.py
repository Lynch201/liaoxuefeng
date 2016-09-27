#201609251559
#lynch.wang

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# fixme:port should be 9999
s.connect(('127.0.0.1', 8000))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
