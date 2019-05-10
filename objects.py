from random import randint
### Random object spawn (Case bleue)

def objet_gain():
    return ["Vol 5 Pièces","Vol étoile","+3","-3"][randint(0,3)]


### Fonctions des Objets utilisables
def vol5(JOUEURS,currentPlayer):    #Vole 5 pièces à l'adversaire choisi
    vol5_possible = recherchePieces(JOUEURS,currentPlayer)
    
    for i in vol5_possible:
        print("<>",i)
    choixAdv = input("A quel joueur voulez vous voler des pièces?:")
    
    while choixAdv not in vol5_possible:
        choixAdv = input("Ce joueur n'est pas dans la liste, veuillez réessayer:")
    return choixAdv

def voletoile(JOUEURS,currentPlayer): #Vole 1 étoile à l'adversaire choisi
    volEtoile_possible = rechercheEtoile(JOUEURS,currentPlayer)
    
    for i in volEtoile_possible:
        print("<>",i)
    choixAdv = input("A quel joueur voulez vous voler une étoile?:")
    
    while choixAdv not in volEtoile_possible:
        choixAdv = input("Ce joueur n'est pas dans la liste, veuillez réessayer:")
    return choixAdv
    
    
def moins_3(JOUEURS,currentPlayer): #Enleve 3 au lancer de dé de l'adversaire choisi
    joueursPossibles = joueurPoss(JOUEURS,currentPlayer)
    
    for i in joueursPossibles:
        print("<>",i)
    choixAdv = input("A quel joueur voulez vous retirer 3 cases?:")
    
    while choixAdv not in joueursPossibles:
        choixAdv = input("Ce joueur n'est pas dans la liste, veuillez réessayer:")
    return choixAdv
    
#Donne la liste des joueurs possédant plus de 5 pièces
def recherchePieces(lstJoueurs,currentPlayer):
    vol5_possible = []
    for i in lstJoueurs:
        if i["pieces"]>=5:
            vol5_possible.append(i["pseudo"])
    if currentPlayer["pseudo"] in vol5_possible:
        vol5_possible.remove(currentPlayer["pseudo"])
    return vol5_possible

#Donne la liste des joueurs possédant au moins 1 étoile
def rechercheEtoile(lstJoueurs,currentPlayer):
    volEtoile_possible = []
    for i in lstJoueurs:
        if i["etoiles"] >= 1:
            volEtoile_possible.append(i["pseudo"])
    if currentPlayer["pseudo"] in volEtoile_possible:
        volEtoile_possible.remove(currentPlayer["pseudo"])
    return volEtoile_possible

#Joueurs possibles (Tout les joueurs sauf celui qui utilise l'objet)
def joueurPoss(lstJoueurs,currentPlayer):
    joueursPossibles = []
    for i in lstJoueurs:
        if i["pseudo"] != currentPlayer["pseudo"]:
                joueursPossibles.append(i["pseudo"])
    return joueursPossibles