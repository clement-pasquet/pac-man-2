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
        mySocket.bind((HOTE, PORT))
    except socket.error:
        print("Liaison du socket UDP à l'adresse et au port choisis a échoué.")
        sys.exit()

    print("Le serveur UDP écoute sur le port {}".format(PORT))

    while True:
        msgClient, adresseClient = mySocket.recvfrom(4096)
        msgClient = msgClient.decode('utf-8')

        if msgClient.lower() == "start":
            # Initialiser la carte du Pac-Man
            pacman = pac.Pacman()
            ghosts = [pac.Fantome() for _ in range(3)]
            for i in range(len(ghosts)):
                
                ghosts[i].x = 1
                ghosts[i].y = 1

                
            current_map = pacman.draw(ghosts)
            msgServeur = bytes(current_map)
            mySocket.sendto(msgServeur, adresseClient)
            

        elif msgClient.lower() in ["droite", "gauche", "avant", "arriere"]:
            if msgClient.lower() == "droite":
                pacman.move_right()
            elif msgClient.lower() == "gauche":
                pacman.move_left()
            elif msgClient.lower() == "avant":
                pacman.move_up()
            elif msgClient.lower() == "arriere":
                pacman.move_down()
            elif msgClient.lower() == "plusdefantome":
                ghosts.append(pac.Fantome())

            for ghost in ghosts:
                ghost.move(pacman)
                if pacman.x == ghost.x and pacman.y == ghost.y:
                    print("Pacman a été touché par un fantôme ! Game over.")
                    mySocket.close()
                    sys.exit()

            current_map = pacman.draw(ghosts)
            msgServeur = bytes(current_map)
            mySocket.sendto(msgServeur, adresseClient)

    print("Serveur fermé.")
    mySocket.close()
    sys.exit()

if __name__ == "__main__":
    serveurUDP_simple()
