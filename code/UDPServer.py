from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1',serverPort))
print 'the server is ready to receive'
i=0
while True:
    message , clientAddress = serverSocket.recvfrom(2048)
    i=i+1
    upperMessage = message.upper()
    modifiedMessage = "you message is {a} ,and you are {d} user".format(a=upperMessage,d=i)
    serverSocket.sendto(modifiedMessage,clientAddress)
