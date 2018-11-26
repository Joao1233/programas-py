# -*- coding: utf-8 -*-
import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
host=""
porta=57000
s.bind((host, porta))
s.listen(2)
while True:
	print("esperando conexão...")
	c, e=s.accept()
	print("Nova conexao de ", e )
	filename="usuario-1.py"
	fyle=open(filename, "rb")
	arquivo=fyle.read(1024)
	c.send(arquivo)
	print("Arquivo enviado...")
	fyle.close()
	c.close()
s.close()
