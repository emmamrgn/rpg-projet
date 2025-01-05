import Menu
from Objets import Objet
from termcolor import colored

class Dague(Objet):
    def __init__(self, nom, valeur=0, degats=0):
        super().__init__(nom, valeur)
        self.degats = degats

    def utiliser_objet(self, combat):
        m = Menu
        choix = m.menu_ennemis(combat.ennemis)
        match choix:
            case 0:
                personnage = combat.joueur
            case _:
                personnage = combat.ennemis[choix-1]
        personnage.statistiques.PV = personnage.statistiques.PV - self.degats
        print(f"{self.nom} utilisé")
        print(colored(self.nom, "cyan"),"utilisée")
        self.retirer_objet(combat.joueur)