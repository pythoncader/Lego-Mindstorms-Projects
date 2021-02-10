# -*- coding: utf-8 -*-
# Ce programme permet de récupérer les informations envoyées par 
# le robot EV3 en utilisant les SOCKETS afin de tracer en temps réel
# des graphiques avec MATPLOTLIB
# ATTENTION : les fenetres graphiques doivent être hors de la console
# préférences / consoleIPython / Graphique / Automatique

import socket                    # ici le client doit se connecter avec l'EV3 (=serveur)
import matplotlib.pyplot as plt  # pour tracer des graphiques

port = 12801                  # doit être identique sur l'EV3 (=serveur)
IPlegoEV3 = '10.50.0.113'        # à modifier si besoin

# construire une connexion socket (famille adresse type internet, protocole TCP)
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# se connecter avec le serveur (adresse IP legoEV3, port d'écoute du serveur)
connexion_avec_serveur.connect((IPlegoEV3, port))
print("Connexion établie avec l'EV3 (= serveur) sur le port {}".format(port))

plt.clf()                                     # nettoyer les anciens points
plt.xlabel('x (mm)') 
plt.ylabel('y (mm)')
plt.title('Position du robot EV3')
plt.axis([-1000,1000,-1000,1000])
msg_recu = connexion_avec_serveur.recv(1024)  # longueur du message <1024    

while msg_recu != b"fin":                     # "fin" enoyé par EV3 
    msg_recu_decode = msg_recu.decode()       # transforme le binaire en string    
    pos = msg_recu_decode.split(',')          # supprime les ,
    print(pos)
    pos = [float(pos[0]),float(pos[1])]       # liste de n string en 2 réel
    plt.scatter(pos[0],pos[1],c='red',marker='+')
    plt.pause(0.001)                          # temps de pause < période d'envoie des messages
    msg_recu = connexion_avec_serveur.recv(1024)  # longueur du message <1024

connexion_avec_serveur.close()                # fermeture de la connexion
print("Fin de connexion avec l'EV3")          # avertissement pour utilisateur