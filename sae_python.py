HOTE = '0.0.0.0'
PORT = 8000

import sys
import socket
import testPacman as pac
import random

def serveurUDP_simple():
    
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        mySocket.bind((HOTE,PORT))
    except socket.error:
        print("Liaison du socket UDP à l'adresse et au port choisit a échoué.")
        sys.exit()
        
    print("Le serveur UDP écoute sur le port {}".format(PORT))
    while 1:
        msgClient, adresseClient = mySocket.recvfrom(1024)

        pacman = pac.Pacman()
        pacman.draw()
        mapi = pacman.map
        ghosts = [pac.Fantome() for _ in range(random.randint(1, 3))]
        if msgClient.lower() == b"start":
            print("msg serveur ici :",mapi)
            msgServeur = bytes(pacman.map)
            print("msg serveur ici :",msgServeur)
            mySocket.sendto(msgServeur, adresseClient)
        #if msgClient.lower() == b"start":
            
        print("Message Client reçu: ", msgClient.decode('utf-8'))
        msgServeur = msgClient
        mySocket.sendto(msgServeur, adresseClient)
        if msgClient.upper() == b"FIN" or msgClient == b"":
            break
    
        msgServeur = msgClient
        mySocket.sendto(msgServeur, adresseClient)
        
        #reglage difficulté
        if msgClient.upper() == b"difficulte max":
            pacman.difficulte = 10
        #déplacements
        if msgClient.upper() == b"droite":
            pacman.move_right()
        elif msgClient.upper() == b"gauche":
            pacman.move_left()
        elif msgClient.upper() == b"avant":
            pacman.move_up()
        elif msgClient.upper() == b"arriere":
            pacman.move_down()
        
    print("Serveur fermé.")
    mySocket.close()
    sys.exit()
    
if __name__ == "__main__":
    serveurUDP_simple()
