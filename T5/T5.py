#!/usr/bin/python
from socket import *
import os

UDP_PORT = 32000

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

#define a porte que vai estabelecer a conexao
#s.bind((UDP_IP ,UDP_PORT))

data = []

for c in range(0,232):
	data.append(c)

data.append(22)
data.append(7)
data.append(64)

dt = bytes(data)

while 1:
	
	print ("\tEnviando mensagem...", dt)
		
	#Send message UDP
	print ("Caracteres enviados: ", len(dt))
	s.sendto(dt, ('localhost', UDP_PORT))
	
	#Receive message UDP
	data, addr = s.recvfrom(1024)
	print ("received message: ", data)
	print ("Caracteres recebidos: ", len(data))