# -*- coding:utf-8 -*-
# ����socket��:
import socket
import threading
import time

myexit = False

def tcplink(sock, addr):
    global myexit
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    myexit = True
    print('Connection from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# �����˿�:
s.bind(('10.253.8.74', 9998))

s.listen(5)
print('Waiting for connection...')

while myexit == False:
    print('0', myexit)
    # ����һ��������:
    sock, addr = s.accept()
    # �������߳�������TCP����:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
print('Server exit')
	
