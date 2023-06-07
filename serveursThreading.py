# -*-coding:utf-8 -*
""" Module contenant les Serveurs
"""

HOTE = '127.0.0.1'      # @IP interfaces => ici lo
PORT =  8000            # n° port écoute du serveur

import sys
import socket
import threading

def serveurTCP_simple():
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        mySocket.bind((HOTE,PORT))
    except socket.error:
        print("Liaison du socket UDP à l'adresse et au port choisit a échoué.")
        sys.exit()
    
    while 1: 
        msgClient, adresseClient = mySocket.recvfrom(1024)
        print( "Client connecté, adresse IP %s, port %s" % (adresseClient[0], adresseClient[1]) )
        msgServeur = msgClient
        mySocket.sendto(msgServeur, adresseClient)


    print("Serveur fermé.")
    mySocket.close() 
    sys.exit()



import socket
import threading

def serveurUDP_parallele():
    class ThreadClient(threading.Thread):
        def __init__(self, data, adresse):
            threading.Thread.__init__(self)
            self.data = data
            self.adresse = adresse

        def run(self):
            nom = self.getName() 
            msgClient = self.data
            print("Message Client %s reçu : %s" % (nom, msgClient.decode('utf-8')))
            if msgClient.upper() == b"FIN" or msgClient == b"":    
                return
            msgServeur = msgClient
            mySocket.sendto(msgServeur, self.adresse)
            print("Connexion %s déconnectée" % nom)

    HOTE = '' # Adresse IP du serveur
    PORT = 8000 # Port d'écoute

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        mySocket.bind((HOTE, PORT))
    except socket.error:
        print("Liaison du socket UDP à l'adresse et au port choisis a échoué.")
        sys.exit()

    print("Le serveur UDP écoute sur le port %d" % PORT)

    while True:
        data, adresse = mySocket.recvfrom(1024)
        th = ThreadClient(data, adresse)
        th.start()
        it = th.getName()
        print("Client %s connecté, adresse IP %s, port %s." % (it, adresse[0], adresse[1]))

    print("Serveur fermé.")
    mySocket.close()
    sys.exit()

if __name__ == "__main__":
    serveurUDP_parallele()

