HOTE = '0.0.0.0'
PORT = 8000

import sys
import socket

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
        
        print("Message Client reçu: ", msgClient.decode('utf-8'))
        if msgClient.upper() == b"FIN" or msgClient == b"":
            break
        if msgClient.upper() == b"id":
            print("prêt à être identifié")
            
        msgServeur = msgClient
        mySocket.sendto(msgServeur, adresseClient)
        
    print("Serveur fermé.")
    mySocket.close()
    sys.exit()
    
if __name__ == "__main__":
    serveurUDP_simple()
