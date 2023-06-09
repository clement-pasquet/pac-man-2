HOTE = '127.0.0.1'
PORT = 8000

import sys
import socket
import os
import keyboard


def clientUDP():
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msgClient = input("Message ? ")
    mySocket.sendto(bytes(msgClient, 'utf-8'), (HOTE, PORT))
    if msgClient == "":
        print("Sortie du programme")
        mySocket.close()
        sys.exit()

    while True:
        if keyboard.is_pressed('z'):
            print("Avancer")
            msgClient = "avant"
        elif keyboard.is_pressed('q'):
            print("Gauche")
            msgClient = "gauche"
        elif keyboard.is_pressed('s'):
            print("Arrière")
            msgClient = "arriere"
        elif keyboard.is_pressed('d'):
            print("Droite")
            msgClient = "droite"

        mySocket.sendto(bytes(msgClient, 'utf-8'), (HOTE, PORT))

        msgServeur, adresseServeur = mySocket.recvfrom(1024)

        print(msgServeur.decode('utf-8'), "Map Pac-Man")

        if msgClient.upper() == "FIN" or msgClient == "":
            break

    print("Fin du programme")
    mySocket.close()
    sys.exit()

if __name__ == "__main__":
    clientUDP()
