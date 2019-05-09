from interface import *
from theme import *
from objects import *
from random import randint
import sys

def gen_Plateau(): #Génération de plateau, (60% Vert / 20% Bleu / 20% Rouge)
    PLATEAU = [1]
    for i in range(31):
        case = randint(0,100)
        if case <= 60:
            PLATEAU.append(1) #Génére une case Verte
        elif case <= 80:
            PLATEAU.append(2) #Génére une case Rouge
        else:
            PLATEAU.append(3) #Génére une case Bleue
    return PLATEAU


def nv_etoile(): #Crée une étoile sur une position aléatoire du plateau
    pos_etoile = randint(0,len(PLATEAU)-1)
    place_etoile(pos_etoile,PLATEAU)
    return pos_etoile

def joueurs(): #Stockage des joueurs
    
    J1={"position":0,"pieces":5,"etoiles":0,"objets":[]}
    J2={"position":0,"pieces":5,"etoiles":0,"objets":[]}
    J3={"position":0,"pieces":5,"etoiles":0,"objets":[]}
    J4={"position":0,"pieces":5,"etoiles":0,"objets":[]}
    MAX_JOUEURS = [J1,J2,J3,J4]
    JOUEURS = []
    
    nbr_joueurs=int(input("Nombre de joueurs :(1 à 4 Joueurs)\n"))
    while nbr_joueurs not in range(1,5):
        print("Le nombre de joueurs n'est pas entre 1 et 4")
        nbr_joueurs=int(input("Nombre de joueurs :(1 à 4 Joueurs)\n"))
        
    for i in range(nbr_joueurs): #Ajoute les dictionnaires pour le nombre de joueurs choisi
        JOUEURS.append(MAX_JOUEURS[i])    


    #Choix des pseudos
    for i in JOUEURS:
        i["pseudo"]=input("Joueur insérez votre pseudo:\n")
    return JOUEURS

def init():
    ##Démarrage de la partie, efface le plateau d'abord
    efface_plateau()
    
    ###Confirmation choix de thème
    theme_q = str(input("Voulez vous utiliser un thème?: (Y=Yes / N=No)"))
    while theme_q.lower() != 'y' and theme_q.lower() != 'n':
        theme_q = str(input("Voulez vous utiliser un thème?: (Y=Yes / N=No)"))
    #Si Y, lance le selecteur de theme
    if theme_q.lower() == 'y':
        theme_select()
    
    cree_plateau(gen_Plateau()) #Dessine le plateau
    nv_etoile() #Place l'étoile sur le plateau
    
    joueurs() #Lance la séléction des joueurs
    
    nbr_tours = int(input("Choisissez le nombre de tours\n"))
    while type(nbr_tours) !=  int:
        print("La valeur entrée n'est pas un nombre.")
        nbr_tours = int(input("Choisissez le nombre de tours\n"))