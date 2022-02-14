import socket
import random
import time
import argparse

parser = argparse.ArgumentParser(description="Uspostavljanje server/klijent veze")
parser.add_argument("host", metavar="", type=str, help="Unesite IP adresu servera")
parser.add_argument("port", metavar="", type=int, help="Unesite port")
protokol = parser.add_mutually_exclusive_group()
protokol.add_argument("-t" ,"--tcp", action="store_true", help="Uspostavlja TCP/IP protokol povezivanja")
protokol.add_argument("-u","--udp", action="store_true", help="Uspostavlja UDP/IP protokol povezivanja")
args = parser.parse_args()
'''
IP adresa, port number, DHT pin, TCP ili UDP protokol
'''

if args.tcp:
	klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	klijent.connect((args.host, args.port))

	poruka_inicijalizacije = "start"
	klijent.send(poruka_inicijalizacije.encode("ascii"))
	'''
	Poruka inicijalizacije
	'''

	while True:
		try:
			message = klijent.recv(1024).decode("ascii")
			if message == "close":
				print(f"Prekinuta konekcija sa: {args.host}!")
				break
			else:	
				print(f"{message}")
				while True: 
					try:
						nova_poruka = input("Unesite novu poruku: ")
						if len(nova_poruka) == 0:
							continue
						else:
							break
					except:
						pass
				klijent.send(nova_poruka.encode("ascii"))
		except:
			pass
	klijent.close()

elif args.udp:
	message = ("Hello, server".encode("ascii"))
	klijent = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	n = 5
	i = 0
	while i < n:
		i += 1
		try:
			klijent.sendto(message, (args.host, args.port))
			time.sleep(0.5)
		except:
			pass

else:
	pass
