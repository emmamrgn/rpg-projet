from Joueur import Joueur
from Ennemi import Ennemi
from EtatPartie import EtatPartie 
import Menu
from termcolor import colored
from MaitreDeJeu import MaitreDeJeu


class Combat:
    def __init__(self, joueur : Joueur, ennemis : Ennemi):
        self.joueur = joueur
        self.ennemis = ennemis
        # self.ennemis = list(ennemis.values())

    def afficher_combat(self):
        self.joueur.afficher_stats_personnage()
        if self.ennemis:
            for ennemi in self.ennemis:
                ennemi.afficher_stats_personnage()
        else:
            print(f"Pas d'ennemis dans le combat")

    def infliger_degats(self, attaquant, defenseur):
        degats = attaquant.statistiques.ATQ - defenseur.statistiques.DEF
        if attaquant.arme and attaquant.arme.attaque:
            degats += attaquant.arme.attaque
        if defenseur.armure:
            for piece_armure in defenseur.armure:
                if piece_armure:
                    degats -= piece_armure.defense
        defenseur.statistiques.PV -= max(0, degats)
        if attaquant == self.joueur:
            a = MaitreDeJeu()
            print(colored(attaquant.nom, "blue"), "inflige", colored(f"{max(0,degats)}", "red"), "dégâts à", colored(f"{defenseur.nom}", "yellow")+ ".")
            print()
            a.attaque("le joueur", "attaque", defenseur.nom, str(degats), True)
        if defenseur == self.joueur:
            a = MaitreDeJeu()
            print(colored(attaquant.nom, "yellow"), "inflige", colored(f"{max(0,degats)}", "red"), "dégâts à", colored(f"{defenseur.nom}", "blue")+ ".")
            print()
            a.attaque(attaquant.nom, "attaque", "le joueur", str(degats), False)


    def determiner_tour(self):
        participants = [self.joueur] + self.ennemis
        # Trier les participants par vitesse (plus élevé en premier)
        participants.sort(key=lambda x: x.statistiques.VIT, reverse=True)
        return participants

    def tour_de_combat(self):
        # print("test tour de combat")
        ordre_des_actions = self.determiner_tour()
        for participant in ordre_des_actions:
            if participant == self.joueur and participant.statistiques.PV > 0:
                cible = self.ennemis[0] if self.ennemis else None
                if cible:
                    self.infliger_degats(self.joueur, cible)
                    if cible.statistiques.PV <= 0:
                        print(colored(f"! {cible.nom} a été vaincu !", "green"))
                        self.ennemis.remove(cible)
            else:
                if participant.statistiques.PV > 0 :
                    self.infliger_degats(participant, self.joueur)
                    if self.joueur.statistiques.PV <= 0:
                        print(colored(f"{self.joueur.nom} a été vaincu!", "red"))
                        break
    
    def commencer_combat(self):
        m = Menu
        choix = m.menu_actions()
        while self.joueur.statistiques.PV > 0 and len(self.ennemis) > 0:
            match choix:
                case 0: # combattre l'ennemi
                    self.tour_de_combat()
                    return choix                    # return choix dans le Manager
                case _: 
                    return choix 
    
    def continuer_combat(self):
        m = Menu
        choix = m.menu_combat_encours()
        while self.joueur.statistiques.PV > 0 and len(self.ennemis) > 0:
            match choix:
                case 0: # combattre l'ennemi
                    self.tour_de_combat()
                    return choix                    # return choix dans le Manager
                case 1: # ouvrir mon inventaire
                    return choix     