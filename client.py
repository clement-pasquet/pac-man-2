
HOTE = '127.0.0.1'
PORT= 8000

import sys
import socket

def clientUDP() :
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	msgClient = input("Message ? ")
	if msgClient == "":
		print("Sortie du programme")
		mySocket.close()
		sys.exit()
	while 1:
		mySocket.sendto(bytes(msgClient, 'utf-8'), (HOTE, PORT))
		
		msgServeur, adresseServeur = mySocket.recvfrom(1024)
		
		print("Echo reçu: ", msgServeur.decode('utf-8'))
		
		msgClient= input("Message ? (sinon taper FIN) ")
		
		if msgClient.upper() == "FIN" or msgClient == "":
			break
	
	print("Fin du programme")
	mySocket.close()
	sys.exit()
	
if __name__ == "__main__":
    clientUDP()
