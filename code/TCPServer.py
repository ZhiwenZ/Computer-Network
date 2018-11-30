#! coding=utf-8
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)                         #1表示了接收的最大连接请求
print 'The server is ready to receive'
while 1:
    connectionSocket , addr = serverSocket.accept()
    sentence=connectionSocket.recv(1024)
    capitiazedSentence = sentence.upper()
    connectionSocket.send(capitiazedSentence)
    connectionSocket.close()