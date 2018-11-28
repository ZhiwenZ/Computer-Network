#! coding=utf-8
from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET , SOCK_DGRAM )      # 第一个变量代表是地址簌，第二个变量代表该套接字是UDP套接字
message = raw_input( 'Input lowercase sentence:' )
clientSocket.sendto(message,(serverName , serverPort))
modifiedMessage , serverAddress =clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()