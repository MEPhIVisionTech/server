import socket
import sys

ip = "localhost"
port = 9999

# создаём сокет для подключения
sock = socket.socket()
sock.connect((ip,port))

# запрашиваем имя файла и отправляем серверу
f_name = 'test'
sock.send((bytes(f_name, encoding = 'UTF-8')))

# открываем файл в режиме байтового чтения
f = open (f_name, "rb")

# читаем строку
l = f.read(1024)

while (l):
    # отправляем строку на сервер
    sock.send(l)
    l = f.read(1024)

f.close()
sock.close()
