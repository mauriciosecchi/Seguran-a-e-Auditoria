#!/usr/bin/python
from time import *
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

print ("%s-%s-%s %s:%s:%s\tEnviando broadcast..." % localtime()[:6])

l = []

for i in range(0,232):
   l.append(i)

l.append(220)
l.append(7)
l.append(64)


#4006dc
#64 6 220
#cadd = "cd7004"

s.sendto(bytes(l) , ('localhost', 32000))

recebido, addr = s.recvfrom(1024)
print ("Recebido %s" % recebido + " len: " + str(len(recebido)))


