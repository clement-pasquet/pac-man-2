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
    
def display_map(map_to_display):
    # Efface le terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Dictionnaire de correspondance des symboles
    symbol_mapping = {
        '|': '|',
        '~': '.',
        'P': 'P',
        'F': 'F',
    }

    # Déterminer la largeur maximale de la carte
    max_width = max(len(row) for row in map_to_display)

    # Affiche chaque ligne de la carte avec les symboles remplacés et ajustés en largeur
    for row in map_to_display:
        processed_row = [symbol_mapping.get(symbol, symbol) for symbol in row]
        padded_row = ''.join(processed_row).ljust(max_width)
        print(padded_row)


def clientUDP():
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msgClient = input("Message ? ")
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
        new_map = msgServeur.decode('utf-8')

        # Mettre à jour la carte du client de manière incrémentale
        client.set_map(new_map)

        # Afficher la carte mise à jour sur le terminal
        map_to_display = client.get_map()
        display_map(map_to_display)

        # Attendre 0.5 seconde entre chaque mise à jour
        time.sleep(0.5)

        if msgClient.upper() == "FIN" or msgClient == "":
            break

    print("Fin du programme")
    mySocket.close()
    sys.exit()

if __name__ == "__main__":
    clientUDP()
