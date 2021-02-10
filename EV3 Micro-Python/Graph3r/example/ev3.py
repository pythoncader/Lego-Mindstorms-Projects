#!/usr/bin/env python3
# Le robot se déplace en effectuant un carré, il scrute l'environnement avec
# le capteur ultrason. Les données sont envoyées en parrallèle (threat transmission_données)
# en établissant une connexion avec le PC (via socket) et le script graphique.py à exécuter sur le PC
# Ce script utilise le module matplotlib pour tracer en temps réel

from ev3dev.ev3 import *      # utiliser la bibliothèque lego
import socket  # ici serveur  # ouvrir une connexion et echanger avec une autre machine
from sys import stderr        # pour réaliser un affichage retour dans VSCode
from time import sleep, time

btn = Button()                # les touches (bouton) de la briques
mD = LargeMotor('outA')       # defini les moteurs
mG = LargeMotor('outD')
                              
print("Attente connexion avec client")
print("Attente connexion avec le client graphique", file=sys.stderr)
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # construire une socket (famille adresse type internet, protocole TCP)
connexion_principale.bind(('', 12801))       # se prépare à écouter (tous clients potentiels, sur le port 12800)
connexion_principale.listen(5)               # ecoute jusqu'à 5 clients avant validation
connexion_avec_client, infos_connexion = connexion_principale.accept()  # bloque le programme tant qu'il n'y a pas de demande client
                                             # renvoie le socket client, (IP client,port client)
print("Connexion OK")
print("Connexion avec le client graphique : ", infos_connexion, file=sys.stderr)    
while not btn.any():                         # tant que pas appuie sur bouton de la brique
    msg_a_envoyer = str(mD.position) + "," + str(mG.position) + ","
    msg_a_envoyer = msg_a_envoyer.encode()   # transforme string en binaire pour l'emission
    connexion_avec_client.send(msg_a_envoyer)
    #sleep(1)                                 # pas de temps en seconde
connexion_avec_client.send(b"fin")
connexion_avec_client.close()                # fin de la connexion au client graphique
print("Fin de la tache de connexion", file=sys.stderr)   
sleep(1)