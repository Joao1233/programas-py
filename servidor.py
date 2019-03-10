# -*- coding: utf-8 -*-
import socket 
mensagem="Connected with server....."
host='127.0.0.1'
port=4000
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
print("Waiting Connection......")
while True:
	c, e=s.accept()
	print("New Connection with : ", e[0])
	c.send(mensagem.encode("ascii"))
	c.close()
