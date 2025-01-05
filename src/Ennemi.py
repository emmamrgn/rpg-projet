from Personnage import Personnage
from termcolor import colored

class Ennemi(Personnage):
    def __init__(self, nom, stats=None, salle_initiale=None, niveau=1):
        super().__init__(nom, stats, salle_initiale)
        self.est_hostile = True

    """def attaquer(self, cible):
        degats = self.stats.force
        print(f"{self.nom} attaque {cible.nom} avec {degats} points de dégâts!")
        cible.recevoir_dégats(degats)

    def defendre(self):
        self.stats.defense += 1"""

    def comportement_aleatoire(self, cible):
        import random
        actions = [self.attaquer, self.defendre]
        action = random.choice(actions)
        if action == self.attaquer:
            action(cible)
        else:
            action()