import curses
from EtatPartie import EtatPartie, TypeEtatPartie

def menu(titre, options, color='white'):
    def character(stdscr):
        
        curses.curs_set(0) 
        stdscr.clear()
        stdscr.refresh()

        # initialisation des couleurs 
        curses.start_color()
        icol = {
            1: 'red',
            2: 'green',
            3: 'yellow',
            4: 'blue',
            5: 'magenta',
            6: 'cyan',
            7: 'white'
        }
        col = {v: k for k, v in icol.items()}
        background_color = curses.COLOR_BLACK 

        # Initialisation des paires de couleurs
        curses.init_pair(1, col[color], background_color)           # choix sélectionné  
        curses.init_pair(2, curses.COLOR_WHITE, background_color)   # normal en blanc
        curses.init_pair(3, curses.COLOR_WHITE, background_color)   # titre en blanc 

        # Initialisation dynamique des couleurs
        attributes = {
            'highlighted': curses.color_pair(1),    # sélection
            'normal': curses.color_pair(2),         # normal
            'title': curses.color_pair(3)           # titre
        }

        current_option = 0
    
        # Logique de menu interactive
        while True:
            stdscr.clear() 
            
            # ajout du titre sur la première ligne de la fenetre du terminal
            stdscr.addstr(0, 0, titre, attributes['title']) 

            # Affichage du menu avec la sélection actuelle
            for i, option in enumerate(options):
                # mettre entre crochet l'option sélectionnée
                if i == current_option:
                    stdscr.addstr(i + 1, 0, f"  [{option}]", attributes['highlighted'])
                else:
                    stdscr.addstr(i + 1, 0, f"  {option}", attributes['normal'])

            # Gestion de la saisie utilisateur
            key = stdscr.getch()

            if key == curses.KEY_UP and current_option > 0:
                current_option -= 1
            elif key == curses.KEY_DOWN and current_option < len(options) - 1:
                current_option += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return current_option

            stdscr.refresh()

    return curses.wrapper(character)

def main_menu():
    return menu('SCHIZO-RPG', ['Jouer', 'Quitter'], 'blue')

def menu_afficher(etat):
    etat.set_afficher_menu()
    return menu("Que faire ?", ["Afficher la Salle", "Afficher mes Statistiques", "Afficher mon Inventaire", "Afficher les Ennemis", "Commencer le Combat" , "Choisir une Sortie", "Quitter le Jeu"], 'blue') 

def menu_actions():
    return menu("Quelle action choisissez-vous ?", ["Combattre l'ennemi","Fuir" ,"Ouvrir mon Inventaire" , "Retour"], 'blue')

def menu_inventaire(inventaire):
    inv = []
    if (inventaire == []): 
        return -1
    for item in inventaire  :
        inv.append(item.nom)
    return menu("Choisissez un objet à utiliser : ", inv, 'blue')

def menu_marchandise(marchandise):
    tab = []
    tab.append("Retour")
    if(marchandise == []):
        return -1
    for item in marchandise:
        print(marchandise.nom + " = " + marchandise.prix)
        tab.append(marchandise.nom + " = " + marchandise.prix)
    return tab("Choisissez un objet à acheter : ", tab, 'blue')

def menu_ennemis(ennemis):
    tab = []
    tab.append("Vous")
    if(ennemis == []):
        return -1
    for en in ennemis:
        tab.append(en.nom)
    return menu("Choisissez un ennemis : ", tab, 'blue')
        
        
if __name__ == "__main__":
    choix = main_menu()
    print(choix)