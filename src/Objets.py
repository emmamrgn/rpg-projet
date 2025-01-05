from enum import Enum
from termcolor import colored
# from Combat import Combat
# from Personnage import Personnage

class TypeObjet(Enum):
    POTION_PV = "POTION DE SOIN"
    POTION_DEF = "POTION DE DEFENSE"
    POTION_ATT = "POTION D'ATTAQUE"


class Objet:
    def __init__(self, nom, valeur=0):
        if nom == 'null':
            nom = "vide"
        else:
            self.nom = nom
        self.valeur = valeur

    def instancier_objet(dictionnaire):
        from Potion import Potion
        from Dague import Dague
        param = dict(**dictionnaire)
        del param ["type"]
        match dictionnaire["type"]:
            case "Potion":
                return Potion(**param)
            case "Dague":
                return Dague(**param)

    def afficher_objet(self):
        print(f"\t > Nom : ", colored(self.nom, "cyan"))
        print(f"\t   Valeur : ", colored(f"{self.valeur}", "yellow"))    

    def retirer_objet(self, perso):
        perso.inventaire.remove(self)

    def utiliser_objet(self, combat):
        print(colored(self.nom, "cyan"),"utilisée")
        self.retirer_objet(combat.joueur)