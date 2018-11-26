import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host="192.168.0.108"
porta=5700
s.connect((host, porta))
filename="/root/Downloads/baixado-servidor.py"
fyle=open(filename, "wb")
fyle.write(s.recv(100))
fyle.close()
s.close()
print("arquivo recebido")

