from termcolor import colored # pip install termcolor, pour colorer le texte

class Personnage:
    def __init__(self, nom, statistiques, arme, armure, inventaire):
        self.statistiques = statistiques
        self.nom = nom
        self.arme = arme
        self.armure = armure
        self.inventaire = inventaire

    def afficher_nom(self):
        print("-", end=" ") 
        print(colored(f"{self.nom}", "red"))

    def afficher_stats_personnage(self):
        print(f"Nom : ", colored(f"{self.nom}", "blue"))         
        print(colored(f"> Stats"))
        self.statistiques.afficher_stats()
        print(colored(f"> Equipements")) 
        if self.arme:
            print(colored(f" -  Arme équipée: ", "white"))
            self.arme.afficher_objet()
        else:
            print(colored(f"> Pas d'arme équipée <", "grey"))
        if self.armure:
            print(colored(f" -  Armure équipée: ", "white"))
            for piece_armure in self.armure:
                piece_armure.afficher_objet() if piece_armure else None
        else: 
            print(colored(f"> Pas d'armure équipée <", "grey"))
        
    def afficher_inventaire(self):
        if self.inventaire:
            print(f"Inventaire: ")
            for objet in self.inventaire:
                objet.afficher_objet()
        else:
            print(colored(f"> Inventaire Vide <", "grey"))

    def est_mort(self):
        return self.statistiques.PV <= 0