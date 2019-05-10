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


def nv_etoile(plt): #Crée une étoile sur une position aléatoire du plateau
    pos_etoile = randint(0,len(plt)-1)
    place_etoile(pos_etoile,plt)
    return pos_etoile

def joueurs(): #Stockage des joueurs
    
    J1={"position":0,"pieces":5,"etoiles":0,"modifier":0,"objets":{"Vol 5 Pièces":0,"Vol étoile":0,"+3":0,"-3":0}}
    J2={"position":0,"pieces":5,"etoiles":0,"modifier":0,"objets":{"Vol 5 Pièces":0,"Vol étoile":0,"+3":0,"-3":0}}
    J3={"position":0,"pieces":5,"etoiles":0,"modifier":0,"objets":{"Vol 5 Pièces":0,"Vol étoile":0,"+3":0,"-3":0}}
    J4={"position":0,"pieces":5,"etoiles":0,"modifier":0,"objets":{"Vol 5 Pièces":0,"Vol étoile":0,"+3":0,"-3":0}}
    MAX_JOUEURS = [J1,J2,J3,J4]
    JOUEURS = []
    
    nbr_joueurs=int(input("Nombre de joueurs :(1 à 4 Joueurs)\n"))
    while nbr_joueurs not in range(1,5) or type(nbr_joueurs) != int:
        print("Le nombre de joueurs n'est pas entre 1 et 4")
        nbr_joueurs=int(input("Nombre de joueurs :(1 à 4 Joueurs)\n"))
        
    for i in range(nbr_joueurs): #Ajoute les dictionnaires pour le nombre de joueurs choisi
        JOUEURS.append(MAX_JOUEURS[i])


    #Choix des pseudos
    for i in JOUEURS:
        i["pseudo"]=input("Joueur insérez votre pseudo:\n")
    return JOUEURS

def setup():
    ##Démarrage de la partie, efface le plateau d'abord
    efface_plateau()
    
    ###Confirmation choix de thème
    theme_q = str(input("Voulez vous utiliser un thème?: (Y=Yes / N=No)"))
    while theme_q.lower() != 'y' and theme_q.lower() != 'n':
        theme_q = str(input("Voulez vous utiliser un thème?: (Y=Yes / N=No)"))
    #Si Y, lance le selecteur de theme
    if theme_q.lower() == 'y':
        theme_select()
    PLATEAU = gen_Plateau()
    cree_plateau(PLATEAU) #Dessine le plateau
    
    JOUEURS = joueurs() #Lance la séléction des joueurs
    
    nbr_tours = int(input("Choisissez le nombre de tours\n"))
    while type(nbr_tours) !=  int and nbr_tours >0:
        print("La valeur entrée n'est pas un nombre.")
        nbr_tours = int(input("Choisissez le nombre de tours\n"))
        
    ##Dessine les personnages sur le plateau
    cree_perso(JOUEURS,PLATEAU)
    return {"Joueurs":JOUEURS,"Turns":nbr_tours,"Plateau":PLATEAU}


def startGame():
    settings = setup()
    
    ### On ressort les variables du dictionnaire
    JOUEURS = settings["Joueurs"]
    nbrTours = settings["Turns"]
    PLATEAU = settings["Plateau"]
    
    pos_etoile = nv_etoile(PLATEAU) #Place l'étoile sur le plateau
    
    ### On a maintenant toutes les variables nécessaires au fonctionnement du jeu
    
    for tourActuel in range(1,nbrTours+1): #Démarrage des tours
        print("========================= TOUR ",tourActuel,"=========================")
        
        for i in JOUEURS: #Parcourt les joueurs un par un
            print("<>",i["pseudo"],end=' ')                 # Formattage correct
            input("appuyez sur Entrée pour lancer le dé") #
            
            ### Check si le joueur possède un objet
            objetsTemp = list(i["objets"].values())
            if any(objetsTemp) != 0: #Le joeurs possède donc au moins un objet, on lui demande s'il veut l'utiliser
                
                rqst = input("Voulez vous utiliser un objet? (Y=Yes / N=No):")
                while rqst.lower() != "y" and rqst.lower() != "n":
                    rqst = input("Voulez vous utiliser un objet? (Y=Yes / N=No):")
                
                if rqst.lower() == "y": #Le joueur veut utiliser un objet, on lui demande lequel
                    
                    comptList = 0
                    for j in list(i["objets"].keys()):
                        print(comptList,end=' • ')
                        print(j,", Quantité:",objetsTemp[comptList])
                        comptList+=1
                        
                    
                    
                    ### Choix d'objet fait, on lance la fonction correspondante
                    choixFait = False
                    while choixFait != True:
                        choixFait = False
                        
                        choixObj = int(input("Donnez le rang de l'objet que vous voulez utiliser: (0,1,2,3) -1 pour annuler le choix"))
                        while type(choixObj) != int and 0 <= choixObj <= 3 and choixObj != -1:
                            choixObj = int(input("Donnez le rang de l'objet que vous voulez utiliser: (0,1,2,3) -1 pour annuler le choix"))
                            
                        if choixObj == 0 and i["objets"]["Vol 5 Pièces"] > 0: ##Vol 5 pièces
                            
                            if len(recherchePieces(JOUEURS,i)) > 0:
                                choixAdv = vol5(JOUEURS,i)
                                for tmp in JOUEURS:
                                    if tmp["pseudo"] == choixAdv:
                                        tmp["pieces"] -= 5
                                        
                                i["pieces"] += 5
                                i["objets"]["Vol 5 Pièces"] -= 1
                                
                                choixFait = True
                            else:
                                print("Aucun choix possible pour cet objet")
        
                        elif choixObj == 1 and i["objets"]["Vol étoile"] > 0: ##Vol d'étoile
                            
                            if len(rechercheEtoile(JOUEURS,i)) > 0: 
                                choixAdv = voletoile(JOUEURS,i)
                                for tmp in JOUEURS:
                                    if tmp["pseudo"] == choixAdv:
                                        tmp["pieces"] -= 5
                                        
                                i["etoiles"] += 5
                                i["objets"]["Vol étoile"] -= 1
                                
                                choixFait = True
                            else:
                                print("Aucun choix possible pour cet objet")
                        
                        elif choixObj == 2 and i["objets"]["+3"] > 0: ## +3 au Dé
                            i["modifier"] += 3
                            i["objets"]["+3"] -= 1
                            
                            choixFait = True
                            
                        elif choixObj == 3 and i["objets"]["-3"] > 0: ## -3 au Dé
                            choixAdv = moins_3(JOUEURS,i)
                            
                            for tmp in JOUEURS:
                                if tmp["pseudo"] == choixAdv:
                                    tmp["modifier"] -= 3
                            
                            i["objets"]["-3"] -= 1
                            choixFait = True
                            
                        elif choixObj == -1:
                            print("Utilisation d'objet annulée")
                            choixFait = True
                        else:
                            print("Vous ne possédez pas l'objet choisi, veuillez réessayer")
                        
                    ###
            lnct_de = randint(1,6) + i["modifier"] #Genere un lancer de dé normal puis y ajouter le modificateur
            ne_bouge_pas = False
            if lnct_de == 0:
                ne_bouge_pas = True
            i["modifier"] = 0
            print(i["pseudo"],"a obtenu: ",lnct_de,"!")
            
            if not ne_bouge_pas:
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
                    
                elif PLATEAU[i["position"]] == 2: ##Case Rouge, + de 3 pieces (Perd 3 pièces)
                    print(i["pseudo"],"Vous aviez:",i["pieces"],"pièces")
                    i["pieces"] -= min(i["pieces"],3)
                    print("Vous avez maintenant:",i["pieces"],"pièces")
                                        
                elif PLATEAU[i["position"]] == 3: ##Case Bleue (Objet aléatoire)
                    nouvObj = objet_gain()
                    i["objets"][nouvObj] += 1
                    print("Vous avez gagné l'objet:",nouvObj)
                    
                if i["position"] == pos_etoile: ##Case étoile
                    
                    confAchat = input("Voulez vous acheter cette étoile (Cout: 5 Pièces): N=Non Y=Oui").upper()
                    while confAchat.upper() != "Y" and confAchat.upper() != "N":
                        confAchat = input("Voulez vous acheter cette étoile (Cout: 5 Pièces): N=Non Y=Oui")
                        
                    if confAchat.upper() == "Y" and i["pieces"] >= 5:
                        i["pieces"] -= 5
                        turtle_star.reset()
                        i["etoiles"] += 1
                        pos_etoile = nv_etoile(PLATEAU)
                        
                    elif confAchat.upper() == "Y" and i["pieces"] < 5:
                        print("Vous n'avez pas assez de pièces")
            elif ne_bouge_pas:
                print(i["pseudo"],"ne bougera pas ce tour!")
    print("========================= FIN DU JEU =========================")
    
    ScoreTime = []
    for i in JOUEURS:
        jActuel = i["pseudo"]
        scoreActuel = i["etoiles"]*2 + i["pieces"]/10
        dct_Temp = {"pseudo":jActuel,"score":scoreActuel}
        ScoreTime.append(dct_Temp)
    SortedScore = sorted(ScoreTime, key=lambda k: k['score'], reverse = True)
    print(SortedScore[0]["pseudo"]," a gagné avec:",SortedScore[0]["score"],"points")
    print("========================= SCORES =========================")
    for i in SortedScore:
        print(i["pseudo"],", Score:",i["score"])
    print("Merci d'avoir joué!")