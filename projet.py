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
bg = 'bg.gif'
screen.addshape(bg)
turtle.Turtle().shape(bg)

### Les joueurs
J1={"position":0,"pieces":0,"etoiles":0,"objets":[]}
J2={"position":0,"pieces":0,"etoiles":0,"objets":[]}
J3={"position":0,"pieces":0,"etoiles":0,"objets":[]}
J4={"position":0,"pieces":0,"etoiles":0,"objets":[]}
MAX_JOUEURS = [J1,J2,J3,J4]
JOUEURS = []
### Initialisation
cree_plateau(PLATEAU)
place_etoile(randint(0,len(PLATEAU)-1),PLATEAU)
nbr_joueurs = int(input("Nombre de joueurs :(1 à 4 Joueurs)"))
for i in range(nbr_joueurs):
    JOUEURS.append(MAX_JOUEURS[i])