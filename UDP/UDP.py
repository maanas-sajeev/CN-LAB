ClientUDP.py
from socket import *
serverName = &quot;127.0.0.1&quot;

6

serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
sentence = input(&quot;\nEnter file name: &quot;)
clientSocket.sendto(bytes(sentence,&quot;utf-8&quot;),(serverName, serverPort))
filecontents,serverAddress = clientSocket.recvfrom(2048)
print (&#39;\nReply from Server:\n&#39;)
print (filecontents.decode(&quot;utf-8&quot;))
# for i in filecontents:
# print(str(i), end = &#39;&#39;)
clientSocket.close()
clientSocket.close()
ServerUDP.py
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((&quot;127.0.0.1&quot;, serverPort))
print (&quot;The server is ready to receive&quot;)
while 1:
sentence, clientAddress = serverSocket.recvfrom(2048)
sentence = sentence.decode(&quot;utf-8&quot;)
file=open(sentence,&quot;r&quot;)
con=file.read(2048)
serverSocket.sendto(bytes(con,&quot;utf-8&quot;),clientAddress)
print (&#39;\nSent contents of &#39;, end = &#39; &#39;)
print (sentence)
# for i in sentence:
# print (str(i), end = &#39;&#39;)
file.close()
