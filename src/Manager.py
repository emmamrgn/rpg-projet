from EtatPartie import EtatPartie
from Stats import Stats
from Personnage import Personnage
from Objets import Objet
from Arme import Arme
from Armure import Armure
from Combat import Combat
from Salle import Salle
import json
import Menu
from EtatPartie import EtatPartie, TypeEtatPartie
from MaitreDeJeu import MaitreDeJeu
import sys
from termcolor import colored # https://pypi.org/project/termcolor/

class Manager:

    def is_enter_pressed():
        print(colored(f"                                                  ", attrs=["underline"]))
        pressed = input(colored(f"Appuyez sur Entrée pour afficher le Menu "))
        print(colored(f"                                                  ", attrs=["underline"]))
        if pressed == "":
            return True
        return False
            
    def quitter_partie():
        print(colored(f"-----------------------------------------------------", "grey"))
        print(colored(f"Vous avez quitté la partie.", "grey"))
        sys.exit()

    def read_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        stat_joueur = Stats(**data["joueur"]["statistiques"])
        
        # Création de l'inventaire
        inventaire = []
        for item_data in data["joueur"]["inventaire"]:
            # gérer le cas si l'objet est une potion (type = potion) ou autre chose
            objet = Objet.instancier_objet(item_data)
            inventaire.append(objet)

        item_data = data["joueur"]["arme"]
        arme_joueur = Arme(**item_data) if item_data else None

        armure_joueur = []
        for item_data in data["joueur"]["armure"]:
            piece_armure = Armure(**item_data) if item_data else None
            armure_joueur.append(piece_armure)

        joueur = Personnage(data["joueur"]["nom"], stat_joueur, inventaire=inventaire, arme=arme_joueur, armure=armure_joueur)

        # Création des ennemis
        ennemis = {}
        for ennemi_data in data["ennemis"]:
            stat_ennemi = Stats(**ennemi_data["statistiques"])
            arme_data = ennemi_data.get("arme", None)
            arme_ennemis = Arme(**arme_data) if arme_data else None

            armure_ennemis = []
            armure_data = ennemi_data.get("armure", [])
            if armure_data:
                for item_data in armure_data:
                    if isinstance(item_data, dict):
                        piece_armure = Armure(**item_data)
                        armure_ennemis.append(piece_armure)
            ennemis[ennemi_data["nom"]] = Personnage(ennemi_data["nom"], stat_ennemi, inventaire=[], arme=arme_ennemis, armure=armure_ennemis)


        # Création des salles
        salles = {}
        for salle_data in data["salles"]:
            personnages = [ennemis[nom] for nom in salle_data.get("ennemis", []) if nom in ennemis]
            salles[salle_data["nom"]] = Salle(salle_data["nom"], salle_data["description"], personnages=personnages)

        # Définition des sorties entre les salles
        for salle_data in data["salles"]:
            salle = salles[salle_data["nom"]]
            for direction, salle_sortie in salle_data.get("sorties", {}).items():
                sortie_salle = salles.get(salle_sortie)
                if sortie_salle:
                    salle.sorties[direction] = sortie_salle

        return joueur, ennemis, salles
    
    def apply(choixMainMenu, etat : EtatPartie, m : Menu):
        if choixMainMenu == 0:  # Jouer
            joueur, ennemis, salles = Manager.read_json('./src/data.json')
            salle_actuelle = salles["Entrée de la grotte"]
            ancienne_salle = salle_actuelle
            choix_affichage = m.menu_afficher(etat)
            while(True):
                while (etat.etatActuel == TypeEtatPartie.MENU_AFFICHAGE):
                    match choix_affichage:
                        case 0:     # choix de afficher salle dans le menu_afficher
                            salle_actuelle.afficher_salle()
                            etat.set_none()
                            if (Manager.is_enter_pressed()):  
                                choix_affichage = m.menu_afficher(etat)
                            break

                        case 1:   # choix de afficher mes stats dans le menu_afficher
                            joueur.afficher_stats_personnage()
                            etat.set_none()
                            if (Manager.is_enter_pressed()):                         
                                choix_affichage = m.menu_afficher(etat)
                            break

                        case 2:     # choix de afficher inventaire dans le menu_afficher
                            joueur.afficher_inventaire()
                            etat.set_none()
                            if (Manager.is_enter_pressed()):                         
                                choix_affichage = m.menu_afficher(etat)
                            break

                        case 3:     # choix de afficher ennemis dans le menu_afficher
                            for ennemi in ennemis.values():
                                ennemi.afficher_stats_personnage()
                                etat.set_none()
                            if (Manager.is_enter_pressed()):                          
                                choix_affichage = m.menu_afficher(etat)
                            break

                        case 4: # choix de commencer combat
                            combat = Combat(joueur, salle_actuelle.personnages)
                            choix_combat = combat.commencer_combat()
# SI LE COMBAT EST ENGAGE, alors le joueur a le choix qu'entre COMBATTRE L'ENNEMI OU INVENTAIRE (etat.COMBAT_EN_COURS,menu: menu_combat_encours(), combat:continuer_combat)
                            match choix_combat:
                                case 0 : # combattre l'ennemi
                                    while(choix_combat == 0):                                
                                        if (Manager.is_enter_pressed()):
                                            choix_combat = combat.commencer_combat()
                                    break
                                case 1 :  # fuir
                                    etat.set_none()                                             
                                    salle_buffer = salle_actuelle
                                    salle_actuelle = ancienne_salle
                                    ancienne_salle = salle_buffer
                                    print(f"Vous avez fuit, vous voici désormais dans", salle_actuelle.afficher_nom())
                                    if (Manager.is_enter_pressed()):                          
                                        choix_affichage = m.menu_afficher(etat)
                                    break
                                case 2 : # inventaire
                                    choix_affichage = m.menu_inventaire(joueur.inventaire)
                                    etat.set_none()
                                    joueur.inventaire[choix_affichage].utiliser_objet(combat)
                                    if (Manager.is_enter_pressed()):                          
                                        choix_affichage = m.menu_afficher(etat)
                                    break
                                case 3 : # retour au menu d'avant 
                                    choix_affichage = m.menu_afficher(etat)
                                    break
                            
                        case 5:     # choix de choisir une sortie dans le menu_afficher
                            etat.set_none()
                            salle_actuelle.afficher_sorties()
                            nouvelle_salle = salle_actuelle.sortir_salle()
                            print(colored(f"Vous entrez dans {nouvelle_salle.nom}", "yellow", attrs=["underline"]))
                            if (Manager.is_enter_pressed()):                         
                                choix_affichage = m.menu_afficher(etat)
                            if nouvelle_salle:
                                ancienne_salle = salle_actuelle
                                salle_actuelle = nouvelle_salle
                            break
                        case 6: # quitter le jeu
                            Manager.quitter_partie()
                        
        elif choixMainMenu == 1:  # Quitter
            Manager.quitter_partie()