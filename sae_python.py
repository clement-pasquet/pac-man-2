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
                if i == 0:
                    ghosts[i].x = 2
                    ghosts[i].y = 17
                if i == 1:
                    ghosts[i].x = 7
                    ghosts[i].y = 17
                if i == 2:
                    ghosts[i].x = 4
                    ghosts[i].y = 1
                if i > 2:
                    ghosts[i].x = 1
                    ghosts[i].y = 1
                ghosts[i].preference = 1

            murs_x = [2,2]
            murs_y = [1,3]
            current_map = pacman.draw(ghosts,murs_x,murs_y)
            msgServeur = bytes(current_map)
            mySocket.sendto(msgServeur, adresseClient)
            

        elif msgClient.lower() in ["droite", "gauche", "avant", "arriere"]:
            if msgClient.lower() == "droite":
                pacman.move_right(murs_x,murs_y)
            elif msgClient.lower() == "gauche":
                pacman.move_left(murs_x,murs_y)
            elif msgClient.lower() == "avant":
                pacman.move_up(murs_x,murs_y)
            elif msgClient.lower() == "arriere":
                pacman.move_down(murs_x,murs_y)
            elif msgClient.lower() == "plusdefantome":
                ghosts.append(pac.Fantome())

            for ghost in ghosts:
                ghost.move(pacman)
                if pacman.x == ghost.x and pacman.y == ghost.y:
                    print("Pacman a été touché par un fantôme ! Game over.")
                    mySocket.close()
                    sys.exit()

            murs_x = [2,2]
            murs_y = [1,3]
            current_map = pacman.draw(ghosts,murs_x,murs_y)
            msgServeur = bytes(current_map)
            mySocket.sendto(msgServeur, adresseClient)

    print("Serveur fermé.")
    mySocket.close()
    sys.exit()

if __name__ == "__main__":
    serveurUDP_simple()
