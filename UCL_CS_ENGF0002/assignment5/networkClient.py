import sys
import socket
from time import sleep 
port=9876
ip='192.168.89.128'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while(True):
    try:
        sock.connect((ip, port))
        break
    except ConnectionRefusedError:
        print("waitingforserver...")
        sock.close()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sleep(2)
while(True):
    try:
        text = input("Enter text: ")
    except EOFError:
        sys.exit()
    encoded_text=text.encode()
    try:
        sock.send(encoded_text)
    except BrokenPipeError:
        print("remote disconnection")
        sys.exit()
