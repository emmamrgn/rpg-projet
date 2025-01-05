import sys
from enum import Enum
from termcolor import colored

class TypeEtatPartie(Enum):
    NONE = "NONE"
    MENU_AFFICHAGE = "MENU_AFFICHAGE"

class EtatPartie:
    def __init__(self, etatActuel: TypeEtatPartie = TypeEtatPartie.NONE):
        self.etatActuel = etatActuel

    def set_afficher_menu(self):
        self.etatActuel = TypeEtatPartie.MENU_AFFICHAGE

    def set_none(self):
        self.etatActuel = TypeEtatPartie.NONE
    
    def set_combat_en_cours(self):
        self.etatActuel = TypeEtatPartie.COMBAT_EN_COURS


    # def recommencer_partie(self): 
    #     if self.etatActuel == TypeEtatPartie.TERMINE:
    #         print(colored(f"Vous avez terminé le donjon ! Félicitations ! Retour au terminal.", "yellow"))
    #         sys.exit()
    #     else :
    #         while True:
    #             confirmation = input("Tapez 'q' pour quitter  ou 'p' pour commencer la partie : \n")
    #             if confirmation.lower() == 'q':
    #                     print(colored(f"Vous avez quitté la partie.", "red"))
    #                     self.etatActuel = TypeEtatPartie.QUIT
    #                     sys.exit()
    #             elif confirmation.lower() == 'p':
    #                 print(f"Vous avez choisi de recommencer une partie.")
    #                 self.set_start_partie()
    #                 break