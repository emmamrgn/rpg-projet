from Objets import Objet
from termcolor import colored

class Arme(Objet):
    def __init__(self, nom, valeur = 0, attaque = 0):
        if nom == 'null' :
            super().__init__("pas d'arme", valeur)
        else :
            super().__init__(nom, valeur)
        self.attaque = attaque
    
    def afficher_objet(self):
        super().afficher_objet()
        print(f"\t Attaque :", colored(self.attaque, "red"))