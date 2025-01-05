from Personnage import Personnage

class Joueur(Personnage):
    def __init__(self, nom, stats=None, salle_initiale=None):
        # Appelle le constructeur de la classe mère (Personnage)
        super().__init__(nom, stats, salle_initiale)
        self.inventaire = []

    # def choisir_action(self):
    #     choix_valide = []
    #     choix_valide[0] = "fuir"
    #     choix_valide[1] = "attaquer"
    #     choix_valide[2] = "soigner"
    #     while True:
    #         choix = input("Choisissez une action : combattre, fuir ou vous soigner \n")
    #         if choix in choix_valide:
    #             return choix
    #         else:
    #             print(f"Choix incorrect, veuillez choisir une action")
