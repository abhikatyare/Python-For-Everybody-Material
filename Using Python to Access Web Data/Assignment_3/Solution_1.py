# Author : Abhishek Katyare
# Date   : 5th September, 2019

import socket

command = 'GET http://data.pr4e.org/intro-short.txt HTTP/2.0\r\n\r\n'.encode()

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('data.pr4e.org',80))
mySocket.send(command)

while True:
    data = mySocket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mySocket.close()