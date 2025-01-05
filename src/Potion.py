# from enum import Enum
# from Personnage import Personnage
# from Combat import Combat
import Menu
from Objets import Objet
from termcolor import colored

class Potion(Objet):
    def __init__(self, nom, valeur=0, soin=0):
        super().__init__(nom, valeur)
        self.soin = soin

    def utiliser_objet(self, combat):
        m = Menu
        choix = m.menu_ennemis(combat.ennemis)
        match choix:
            case 0:
                personnage = combat.joueur
            case _:
                personnage = combat.ennemis[choix-1]
        personnage.statistiques.PV = min(personnage.statistiques.PVMAX, personnage.statistiques.PV + self.soin)
        print(colored(self.nom, "cyan"),"utilisée")
        self.retirer_objet(combat.joueur)