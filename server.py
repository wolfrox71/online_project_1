import socket
import sys
from _thread import start_new_thread
from infomation import infomation

info = infomation()

server = info.server
port = info.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved: ", reply)
                reply = "<p> Something </p>"
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break
    print("connection closed")
    conn.close()
try:
    s.bind((server,port))
except socket.error as e:
    print(str(e))

s.listen(2)

print("Waiting for connections...")

while True:
    conn, addr = s.accept()
    print(f"Connected to {addr}")
    start_new_thread(threaded_client, (conn,))
