from Manager import Manager
import Menu
from EtatPartie import EtatPartie, TypeEtatPartie

def main():
    m = Menu
    etat = EtatPartie(TypeEtatPartie.NONE)

    choixMainMenu = m.main_menu()
    Manager.apply(choixMainMenu, etat, m)
        
if __name__ == "__main__":
    main()