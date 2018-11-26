# -*- coding: utf-8 -*-
import socket 
import os

host = "192.168.0.108"
port=2002

msg="Ola a todos que estão no meu servidor pra conversar . . . "

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
print("Servidor ativo")
s.listen(5)

while True: 
	c, e=s.accept()
	c.send(msg)
	c.close()



