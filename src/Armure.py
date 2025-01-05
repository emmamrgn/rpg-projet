from Objets import Objet
from termcolor import colored

class Armure(Objet):
    def __init__(self, nom, valeur=0, defense=0, type='null'):
        if nom == 'null':
            super().__init__("pas de piece", valeur)
        else :
            super().__init__(nom, valeur)
        self.defense = defense
        #Un type sera "casque/torse/jambiere/pieds" ou null
        self.type = type
    
    def afficher_objet(self):
        super().afficher_objet()
        print(f"\t Défense :", end=" ")
        print(colored(f"{self.defense}", "green"))
        print(colored(f"\t   Type : {self.type}", "grey"))