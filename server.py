import socket
import sys

# создаём сокет и связываем его с IP-адресом и портом

sock = socket.socket()
ip = "localhost"
port = 9999
sock.bind((ip, port))

# сервер ожидает передачи информации
sock.listen(10)

while True:
    # начинаем принимать соединения
    conn, addr = sock.accept()

    # выводим информацию о подключении
    print('connected:', addr)

    # получаем название файла
    name_f = (conn.recv(1024)).decode ('UTF-8')

    # открываем файл в режиме байтовой записи в отдельной папке 'sent'
    f = open('sent/' + name_f,'wb')

    while True:

        # получаем байтовые строки
        l = conn.recv(1024)

        # пишем байтовые строки в файл на сервере
        f.write(l)

        if not l:
            break

    f.close()
    conn.close()

    print('File received')

sock.close()
