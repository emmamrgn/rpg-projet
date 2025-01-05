from Personnage import Personnage
import Menu
from EtatPartie import EtatPartie, TypeEtatPartie
from termcolor import colored # pip install termcolor, pour colorer le texte


class Marchand(Personnage):
    def __init__(self, nom, statistiques, arme, armure, inventaire, marchandise):
        super.__init__(nom, statistiques, arme, armure, inventaire)
        self.marchandise = marchandise

    def afficher_marchandise(self):
        if self.marchandise:
            print("{self.nom} vend : ")
            for objet in self.marchandise:
                objet.afficher_objet()
        else:
            print(colored(f"> Inventaire Vide <", "grey"))

    def acheter_objet(self, joueur):
        m = Menu
        e = EtatPartie()
        if self.marchandise:
            m.menu_inventaire(self.marchandise)
