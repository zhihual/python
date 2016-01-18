# -*- coding:utf-8 -*-

# ����socket��:
import socket

# ����һ��socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ��������:
s.connect(('www.liaoxuefeng.com', 80))
# ��������:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# ��������:
buffer = []
while True:
    # ÿ��������1k�ֽ�:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# �ر�����:
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# �ѽ��յ�����д���ļ�:
with open('baidu.html', 'wb') as f:
    f.write(html)