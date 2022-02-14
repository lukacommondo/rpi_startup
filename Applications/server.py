sys.path.append("/home/pi/Modules")
'''
Dodavanje foldera sa modulima u python path
'''
import socket
import time
from dht_senzor import DHT_22
import argparse


parser = argparse.ArgumentParser(description="Uspostavljanje server/klijent veze")
parser.add_argument("host", metavar="host", type=str, help="Unesite IP adresu servera")
parser.add_argument("port", metavar="port", type=int, help="Unesite port")
parser.add_argument("dht_pin", metavar="dht_pin", type=int, help="Unesite pin na kojeg je spojen DHT senzor")
protokol = parser.add_mutually_exclusive_group()
protokol.add_argument("-t" ,"--tcp", action="store_true", help="Uspostavlja TCP/IP protokol povezivanja")
protokol.add_argument("-u","--udp", action="store_true", help="Uspostavlja UDP/IP protokol povezivanja")
'''
IP adresa, port number, DHT pin, TCP ili UDP protokol
'''
args = parser.parse_args()


if args.tcp:
	'''
	AF_INET = IPv4, SOCK_STREAM = TCP protokol
	'''
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((args.host, args.port))
	#Red čekanja za spajanje na server socket
	server.listen(5)
	
	while True:
		communication_socket, address = server.accept()
		print(f"Spojeno na klijenta : {address}!")
		'''Osluškivanje spojenog klijenta
		'''
		while True:
			'''
			Klijent salje serveru inicijalnu poruku
			Server odgovara u skladu sa conditionals
			Buffer = 1024
			'''
			message = communication_socket.recv(1024).decode("ascii")
			print(f"{message}")
			if message == "start":
				communication_socket.send(f"Uspjesno povezivanje na: {args.host}!".encode("ascii"))
			
			elif message == "ping":
				communication_socket.send(f"pong".encode("ascii"))
			
			elif message == "dht":
				'''
				Definiranje pina na kojeg je spojen DHT senzor
				Spremanje i slanje rezultata mjerenja
				'''
				senzor = DHT_22(args.dht_pin)
				rezultati = senzor.temp_vlaga()
				communication_socket.send(f"{rezultati}".encode("ascii"))
				
			elif message == "close":
				communication_socket.send(f"close".encode("ascii"))
				break
			
			else:
				communication_socket.send(f"?".encode("ascii"))

		communication_socket.close()
		print(f"Prekinuta konekcija sa klijentom: {address}!")

elif args.udp:
	'''
	AF_INET = IPv4, SOCK_DGRAM = UDP protokol
	'''
	server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server.bind((args.host, args.port))
	
	while True:
		communication_socket, address = server.recvfrom(1024)
		print(f"Message: {communication_socket}")

else:
	pass





