from random import randint
### Random object spawn (Case bleue)

def objet_gain():
    return ["Vol 5 Pièces","Vol étoile","+3","-3"][randint(0,3)]


### Fonctions des Objets utilisables
def vol5():    #Vole 5 pièces à l'adversaire choisi
    choixAdv = input("A quel joueur voulez vous voler des pièces?:")

def voletoile(): #Vole 1 étoile à l'adversaire choisi
    choixAdv = input("A quel joueur voulez vous voler une étoile?:")
    
def plus_3(): #Ajoute 3 au lancer de dé
    return print("...")

def moins_3(): #Enleve 3 au lancer de dé de l'adversaire choisi
    choixAdv = input("A quel joueur voulez vous enlever 3 cases?:")