import socket
from infomation import infomation

info = infomation()

class network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = info.server
        self.port = info.port
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except Exception as e:
            print(e)
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            print(f"Sent: {data}")
            return self.client.recv(2048).decode()
        
        except socket.error as e:
            print(e)

n = network()

to_send = ""

while to_send.lower() not in ["exit","quit"]:
    to_send = input("Type something to send:\n")
    print(f"Receved: {n.send(to_send)}")