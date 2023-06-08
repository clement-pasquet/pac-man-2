
HOTE = '192.168.1.122'
PORT= 8000

import os
import random
import sys
import socket
if os.name == 'nt':
    import msvcrt
else:
    import tty
    import termios
    import sys

    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def clientUDP() :
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	msgClient = input("Quelle difficulté ? ")
	if msgClient == "":
		print("Sortie du programme")
		mySocket.close()
		sys.exit()
	while 1:
		mySocket.sendto(bytes(msgClient, 'utf-8'), (HOTE, PORT))
		
		msgServeur, adresseServeur = mySocket.recvfrom(1024)
		
		print("Echo reçu: ", msgServeur.decode('utf-8'))
		
		if os.name == 'nt':
			key = msvcrt.getch().decode('utf-8')
		elif os.name != 'nt':
			try : 
				key = getch()
			except :
				print("")
		if key == 'a' or key == 'c':
			break
		elif key == 'q':
			msgClient =b"gauche"
		elif key == 'd':
			msgClient =b"droite"
		elif key == 'z':
			msgClient =b"avant"
		elif key == 's':
			msgClient =b"arriere"

		
		if msgClient.upper() == "FIN" or msgClient == "":
			break
	
	print("Fin du programme")
	mySocket.close()
	sys.exit()
	
if __name__ == "__main__":
    clientUDP()
