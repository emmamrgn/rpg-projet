from Personnage import Personnage
from Objets import Objet
from Combat import Combat
from termcolor import colored
from MaitreDeJeu import MaitreDeJeu

class Salle:
    def __init__(self, nom, description=None, sorties=None, personnages=None, objets=None):
        self.nom = nom
        self.description = description if description else "pas de description"
        self.sorties = sorties if sorties else {} #dictionnaire pour les sorties (ajouté dynamiquement quand on définit une sortie)
        #Une sortie sera "est, ouest, nord, sud" et sera une paire de type : "est : salle2"
        self.personnages = personnages if personnages else [] #si pas de personnages, tableau vide
        self.objets = objets if objets else [] #si pas de personnages, tableau vide

    def afficher_nom(self):
        return colored(f"[" + self.nom + "]", "magenta")

    def afficher_salle(self):
        a = MaitreDeJeu()
        a.nouvelle_salle(self.personnages, self.objets)
        print(self.description)
        if self.sorties:
            for direction, salle in self.sorties.items():
                print(f"La sortie",  colored("[" + direction + "]", "blue"), f"mène à", colored("[" + salle.nom + "]", "magenta"))
        else:
            print(f"Pas de sorties disponible") #Pas censé arriver
        if self.personnages:
            for personnage in self.personnages:
                print(colored(f"Personnages : "))
                personnage.afficher_nom()
        else:
            print(colored(f"Pas de personnages dans la salle", "grey"))
        if self.objets:
            for objet in self.objets:
                objet.afficher_objet()
        else:
            print(colored(f"Pas d'objet dans la salle", "grey"))

    def sortir_salle(self):
        if not self.sorties:
            print(f"Pas de sorties disponible") #Pas censé arriver
            return None
        
        while True: #Tant que le joueur n'a pas chosis où aller recommencer la séléction de la salle suivante
            choix = input("Choisissez une direction pour sortir de la salle \n") #affiche la question au joueur et prend en compte ce qu'il écrit
            #ajouter .strip à la fin pour ne pas prendre les espaces en début et fin de chaine
            #ajouter .lower pour transformer les majuscules en minuscules
            if choix in self.sorties:
                return self.sorties[choix] #retourne la salle associés à la direction
            else:
                print(f"Direction invalide, veuiller saisir une direction valide")

    def afficher_sorties(self):
        if self.sorties:
            a = MaitreDeJeu()
            a.donne_sorties(self.sorties)
            for direction, salle in self.sorties.items():
                print(f"La sortie", colored("[" + direction + "]", "blue"), f"mène à", colored("[" + salle.nom + "]", "magenta"))
    
    # Quand on entre dans une salle on a la description de celle ci, si il y'a des ennemis on lance (pour l'instant de façon obligatoire) un combat
    # Une fois qu'il n'y a plus de combat en cours on sort de la salle (la fonction renvoie la nouvelle salle qu'à choisis le joueur)
    def entrer_salle(self, joueur):
        self.afficher_salle()
