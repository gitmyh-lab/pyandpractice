import socket
HOST = 'localhost'
PORT = 10888
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = "你好！"
while data:
    s.sendto(data.encode('utf-8'),(HOST,PORT))
    if data == 'bye':
        break
    data,addr = s.recvfrom(512)
    print("Receive from server:\n",data.decode('utf-8'))
    data = input('please input a info:\n')
s.close()