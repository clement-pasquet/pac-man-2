import sys
import socket
import os
import keyboard
import time

HOTE = '127.0.0.1'
PORT = 8000

class GameClient:
    def __init__(self):
        self.map = None
        self.score = 0

    def set_map(self, new_map):
        # Convertir la nouvelle carte en une liste de listes
        new_map = [list(row) for row in new_map]

        # Effectuer une mise à jour incrémentale de la carte
        if self.map is None:
            self.map = new_map
        else:
            rows = min(len(self.map), len(new_map))
            cols = min(len(self.map[0]), len(new_map[0]))

            for i in range(rows):
                for j in range(cols):
                    if new_map[i][j] != self.map[i][j]:
                        self.map[i][j] = new_map[i][j]

    def get_map(self):
        # Retourne une copie de la carte actuelle
        return [row[:] for row in self.map]
    
    def update_score(self, increment):
        self.score += increment

def display_map(map_to_display, score):
    os.system('cls' if os.name == 'nt' else 'clear') # Efface le terminal

    print("Score:", score)
    for item in map_to_display:
        if item == ['\n']:
            print()
        else:
            print(item[0], end='')

def clientUDP():
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msgClient = input("Message ? ( start ) ")
    mySocket.sendto(bytes(msgClient, 'utf-8'), (HOTE, PORT))
    if msgClient == "":
        print("Sortie du programme")
        mySocket.close()
        sys.exit()

    client = GameClient()

    while True:
        if keyboard.is_pressed('z'):
            print("Avancer")
            msgClient = "avant"
            client.update_score(1)
        elif keyboard.is_pressed('q'):
            print("Gauche")
            msgClient = "gauche"
            client.update_score(1)
        elif keyboard.is_pressed('s'):
            print("Arrière")
            msgClient = "arriere"
            client.update_score(1)
        elif keyboard.is_pressed('d'):
            print("Droite")
            msgClient = "droite"
            client.update_score(1)
        elif keyboard.is_pressed('c'):
            sys.exit()
        elif keyboard.is_pressed('esc'):
            sys.exit()
        



        mySocket.sendto(bytes(msgClient, 'utf-8'), (HOTE, PORT))

        msgServeur, adresseServeur = mySocket.recvfrom(4096)
        new_map = msgServeur.decode('utf-8')

        # Mettre à jour la carte du client de manière incrémentale
        client.set_map(new_map)

        if client.score == 50:
            print("Vous avez gagné !")
            mySocket.close()
            sys.exit()


        # Afficher la carte mise à jour et le score sur le terminal
        map_to_display = client.get_map()
        display_map(map_to_display, client.score)

        # Attendre 0.5 seconde entre chaque mise à jour
        time.sleep(0.1)

        if msgClient.upper() == "FIN" or msgClient == "":
            break

    print("Fin du programme")
    mySocket.close()
    sys.exit()

if __name__ == "__main__":
    clientUDP()
