#！coding=utf-8
from  socket import  *
serverName = 'servername'
serverPort = 12000
clientSocket = socket(AF_INET , SOCK_STREAM)         #SOCK_STREAM类型
clientSocket.connect(( serverName,serverPort ))         #相比UDP,TCP多一行connetction
sentence = raw_input( 'Input lowercase sentence:' )
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()