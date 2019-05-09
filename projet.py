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
screen.addshape(bg) #Ajoute l'arrière-plan
pos_etoile = randint(0,len(PLATEAU)-1)
def nv_etoile():
    place_etoile(pos_etoile,PLATEAU)
    
#Fct des objets
def vol5():    #Vole 5 pièces à l'adversaire choisi
    choixAdv = input("A quel adversaire voulez vous voler des pièces?:")
    
    
#Fct Objet aléatoire
def objet_gain():
    return ["Vol 5 Pièces","Vol étoile","+3","-3"][randint(0,3)]

def initialisation():
    
    efface_plateau()
    
    ###Place le plateau
    turtle.Turtle().shape(bg)
    cree_plateau(PLATEAU)
    
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
    while nbr_joueurs not in range(1,5):
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
        print("*--------------------------*\nTour",tour,"\n*--------------------------*")
        for i in JOUEURS:
            print(i["pseudo"],end=' ')
            input("Appuyez sur Entrée pour continuer")
            
            if len(i["objets"])!=0:
                comptList=0
                print('Vos objets:')
                
                for j in i["objets"]:
                    print(comptList,end=' •')
                    comptList+=1
                    print(j)
                    
                choixObj=int(input("Donnez le numéro de l'objet que vous voulez utiliser: -1 pour annuler."))
                while choixObj<=-1 and choixObj > len(i["objets"])-1:
                    choixObj=int(input("Donnez le numéro de l'objet que vous voulez utiliser: -1 pour annuler."))
                    
                if choixObj == -1:
                    print('Aucun objet utilisé')
                    
                elif i["objets"][choixObj] == "Vol 5 Pièces":
                    del i["objets"][choixObj]
                    i["pieces"]+=5
                    vol5()
                    
                elif i["objets"][choixObj] == "Vol étoile":
                    del i["objets"][choixObj]
                    voletoile()
                    
                elif i["objets"][choixObj] == "+3":
                    del i["objets"][choixObj]
                    plus_3()
                    
                elif i["objets"][choixObj] == "-3":
                    del i["objets"][choixObj]
                    moins_3()
                    
            lnct_de = randint(1,6) ##Réalise un lancement de dé
            print("*--------------------------*\n",i["pseudo"],"a obtenu: ",lnct_de,"!")
            for p in range(lnct_de):
                i["position"] += 1
                if i["position"] == 32: ##Lorsque la position atteint 32 on remet les joueurs sur la case de départ (Pos 0)
                    i["position"] = 0
                bouge_perso(JOUEURS,PLATEAU) #Fonction de interface.py pour bouger les joueurs sur le plateau
            
            #Perso Bouge, conditions sur case d'arrivée
            if PLATEAU[i["position"]] == 1: ##Case Verte (Gagne 3 pièces)
                print(i["pseudo"],"Vous aviez:",i["pieces"],"pièces")
                i["pieces"] += 3
                print("Vous avez maintenant:",i["pieces"],"pièces")
                
            elif PLATEAU[i["position"]] == 2 and i["pieces"]>=3: ##Case Rouge, + de 3 pieces (Perd 3 pièces)
                print(i["pseudo"],"Vous aviez:",i["pieces"],"pièces")
                i["pieces"] -= 3
                print("Vous avez maintenant:",i["pieces"],"pièces")
                
            elif PLATEAU[i["position"]] == 2 and i["pieces"]<3: ##Case Rouge, - de 3 pieces (Perd 3 pièces)
                print(i["pseudo"],"Vous aviez:",i["pieces"],"pièces")
                i["pieces"] = 0
                print("Vous avez maintenant:",i["pieces"],"pièces")
                
            elif PLATEAU[i["position"]] == 3: ##Case Bleue (Objet aléatoire)
                nouvObj = objet_gain()
                i["objets"].append(nouvObj)
                print("Vous avez gagné un objet")
                print(i["objets"])
                
            if i["position"] == pos_etoile: ##Case étoile
                
                confAchat = input("Voulez vous acheter cette étoile (Cout: 5 Pièces): N=Non Y=Oui").upper()
                while confAchat != "Y" and confAchat != "N":
                    confAchat = input("Voulez vous acheter cette étoile (Cout: 5 Pièces): N=Non Y=Oui")
                    
                if confAchat == "Y" and i["pieces"] >= 5:
                    i["pieces"] -= 5
                    turtle_star.reset()
                    i["etoiles"] += 1
                    nv_etoile()
                    
                elif confAchat == "Y" and i["pieces"] < 5:
                    print("Vous n'avez pas assez de pièces")