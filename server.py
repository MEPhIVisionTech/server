# Код сервера
import socket
import struct

def receive_file_size(sck: socket.socket):
    # Эта функция обеспечивает получение байтов, 
    # указывающих на размер отправляемого файла, 
    # который кодируется клиентом с помощью 
    # struct.pack(), функции, которая генерирует 
    # последовательность байтов, представляющих размер файла.
    fmt = "<Q"
    expected_bytes = struct.calcsize(fmt)
    received_bytes = 0
    stream = bytes()
    while received_bytes < expected_bytes:
        tmp = sck.recv(expected_bytes - received_bytes)
        stream += tmp
        received_bytes += len(tmp)
    filesize = struct.unpack(fmt, stream)[0]
    return filesize


def receive_file(sck: socket.socket, filename):
    # Сначала считываем из сокета количество 
    # байтов, которые будут получены из файла.
    filesize = receive_file_size(sck)
    # Открываем новый файл для сохранения
    # полученных данных.
    with open(filename, "wb") as f:
        received_bytes = 0
        # Получаем данные из файла блоками по
        # 1024 байта до объема
        # общего количество байт, сообщенных клиентом.
        while received_bytes < filesize:
            tmp = sck.recv(1024)
            if tmp:
                f.write(tmp)
                received_bytes += len(tmp)



with socket.create_server(("localhost", 8080)) as server:
    print("Ожидание клиента...")
    conn, address = server.accept()
    print(f"{address[0]}:{address[1]} подключен.")
    print("Получаем файл...")
    receive_file(conn, "sent/image-received.png")
    print("Файл получен.")
print("Соединение закрыто.")
