#### Structures de données
## Le plateau de jeu est déterminé par une liste d’entiers. 
## Ainsi, une position sur le plateau correspond à l’indice d’un élément 
## de la liste (la position 0 par exemple est représentée par le premier élément de la liste).
## 
##
##
##
##
##
####
from interface import *
from random import randint
import sys
PLATEAU = [3,3,2,1,2,3,2,1,2,1,3,1,2,1,2,1,2,1,2,2,3,1,2,3,1,2,1,2,2,1,3,2]
### Arrière-plan
bg = 'background.gif'
screen.addshape(bg)
turtle.Turtle().shape(bg)
cree_plateau(PLATEAU)
def nv_etoile():
    pos_etoile = randint(0,len(PLATEAU)-1)
    place_etoile(pos_etoile,PLATEAU)
    
def initialisation():
    ### Les joueurs
    J1={"position":0,"pieces":5,"etoiles":0,"objets":[]}
    J2={"position":0,"pieces":5,"etoiles":0,"objets":[]}
    J3={"position":0,"pieces":5,"etoiles":0,"objets":[]}
    J4={"position":0,"pieces":5,"etoiles":0,"objets":[]}
    MAX_JOUEURS = [J1,J2,J3,J4]
    JOUEURS = []

    ### Initialisation
    nv_etoile()
    ##Vérification du nombre de joueurs
    nbr_joueurs=int(input("Nombre de joueurs :(1 à 4 Joueurs)\n"))
    while nbr_joueurs not in (1,2,3,4):
        print("Le nombre de joueurs n'est pas entre 1 et 4")
        nbr_joueurs=int(input("Nombre de joueurs :(1 à 4 Joueurs)\n"))
        
    for i in range(nbr_joueurs): #Ajoute les dictionnaires pour le nombre de joueurs donnés
        JOUEURS.append(MAX_JOUEURS[i])    

    #Choix des pseudos
    for i in JOUEURS:
        i["pseudo"]=input("Joueur insérez votre pseudo:\n")
    #Choix du nombre de tours
    nbr_tours = int(input("Choisissez le nombre de tours\n"))

    #Création des persos
    cree_perso(JOUEURS,PLATEAU)

    ### Début du jeu
    #Lancement de dé
    for tour in range(nbr_tours+1):
        print("Tour",tour)
        for i in JOUEURS:
            lnct_de = randint(1,6)
            print(i["pseudo"],"a obtenu: ",lnct_de,"!")
            for p in range(lnct_de):
                i["position"] += 1
                if i["position"] == 32:
                    i["position"] = 0
                bouge_perso(JOUEURS,PLATEAU)