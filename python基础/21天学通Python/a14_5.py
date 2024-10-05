import socketserver
HOST = 'localhost'
PORT = 10888
class MyTcpHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            if not data:
                Server.shutdown()
                break
            print('Receive Data:',data.decode('utf-8'))
            self.request.send(data)
        return
Server = socketserver.TCPServer((HOST,PORT),MyTcpHandler)
Server.serve_forever()