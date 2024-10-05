import socket
HOST = 'localhost'
PORT = 10888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = "你好！"
while data:
    s.sendall(data.encode('utf-8'))
    data = s.recv(512)
    print("Receive from server:\n",data.decode('utf-8'))
    data = input('please input a info:\n')
s.close()