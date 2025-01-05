# Notre RPG TEXTUEL : RPG.GOUV
**Nous avons développer et tester notre RPG uniquement sous Linux et WSL et nous avons utilisé Python et ses librairies .**


## Objectifs 

RPG.GOUV est un jeu de rôle textuel où le joueur intéragit avec un maître de jeu. Le maître de jeu est un modèle de langage (LLM), il va guider le joueur tout au long du jeu en générant des descriptions créatives des événements du jeu, et en répondant à ses actions.


## Sommaire 

1. [Prérequis](#pre)
2. [Installation du Jeu](#dl)
3. [Exécution du Jeu](#exec)
4. [Organisation des répertoires](#orga)
5. [Développeurs](#dev)

<div id="pre"> 

## Prérequis

- Python est nécessaire pour exécuter le jeu. 
    - Se rendre sur la page de [Download de Python](https://www.python.org/downloads/)
- MINGW (ou un autre compilateur C++ comme CMake) est nécessaire pour charger un modèle (utilisation de llama_cpp). 
    - Se rendre sur la page de [Download de MINGW](https://www.mingw-w64.org/downloads/)

</div>


<div id="dl"> 

## Installation du Jeu

### 0. Si WSL et Python 3.12 (ou supérieur) :
- Se créer un environnement virtuel et exécuter le jeu dedans. 

### 1. Cloner le dépôt :
Ouvrir un terminal et exécuter  :

```bash
git clone https://forge.univ-lyon1.fr/p2018177/lifprojet.git
cd lifprojet
```




###  2. Installer les dépendances :
 *(Vérifier de bien être dans le répertoire ``lifprojet/``)*
- **Dans le terminal :** \
    ``pip install -r requirements.txt``  ou  ``pip3 install -r requirements.txt``
    


### 3. Charger un modèle :
*Depuis le terminal, veiller à bien être dans ``lifprojet/`` :*

- [Llama-3.2-3B](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF) : 3 milliards de paramètres
```bash
python3 ./load_llm_3B.py
```

> **Après l'exécution de la commande dans le terminal, le chemin vers le modèle doit  apparaitre une fois que le modèle a été chargé :** 

```bash
# Exemple :
> jiaxi@PC:~/lifprojet$ python3 ./load_llm_3B.py
> Llama-3.2-3B-Instruct-Q4_K_M.gguf: 100%|
llama_model_loader: ...
/home/jiaxi/.cache/huggingface/hub/models--bartowski--Llama-3.2-3B-Instruct-GGUF/snapshots/5ab33fa94d1d04e903623ae72c95d1696f09f9e8/./Llama-3.2-3B-Instruct-Q4_K_M.gguf
```

> NB : *Si le chemin vers le modèle n'apparait pas, ré-exécuter la commande précédente, il devrait apparaître*


###  4. Créer un fichier `model_path.py` dans le répertoire `src` et y mettre le chemin vers le modèle:


```python
# src/model_path.py
MODEL_PATH = "chemin/vers/le/modele"
```
```python
# Exemple :
# MODEL_PATH = "/home/jiaxi/.cache/huggingface/hub/models--bartowski--Llama-3.2-3B-Instruct-GGUF/snapshots/5ab33fa94d1d04e903623ae72c95d1696f09f9e8/Llama-3.2-3B-Instruct-Q4_K_M.gguf"
```

</div>

<div id="exec">

## Exécution du Jeu

> *(Vérifier de bien être dans le répertoire ``lifprojet/``)*

- Pour lancer le jeu, exécutez le fichier `main.py`:
    ```bash
    python3 ./src/main.py
    ```
    ou
    ```bash
    python3 ./src/main.py
    ```

</div>

<div id="orga">

## Organisation des répertoires et des fichiers

```plaintext
src/
  .env                  # Fichier de configuration pour l'API du LLM
  Arme.py               # Classe et fonctions pour les armes
  Armure.py             # Classe et fonctions pour les armures
  Combat.py             # Logique de combat du jeu
  Dague.py              # Classe et fonctions pour les dagues
  data.json             # Fichier de données JSON utilisé par le jeu
  Enigme.py             # Classe et fonctions pour les énigmes
  Ennemi.py             # Classe et fonctions pour les ennemis
  Equipement.py         # Classe et fonctions pour l'équipement
  EtatPartie.py         # Classe et fonctions pour l'état de la partie
  Inventaire.py         # Classe et fonctions pour l'inventaire
  Joueur.py             # Classe et fonctions pour le joueur
  main.py               # Point d'entrée principal du jeu
  MaitreDeJeu.py        # Classe qui gère le maître de jeu (LLM)
  Manager.py            # Classe qui gère l'initialisation du jeu
  Marchand.py           # Classe et fonctions pour les marchands
  Menu.py               # Classe et fonctions pour les menus du jeu
  model_path.py         # Chemin vers les modèles utilisés par le jeu
  Objets.py             # Classe et fonctions pour les objets
  Partie.py             # Classe et fonctions pour la gestion des parties
  Personnage.py         # Classe et fonctions pour les personnages
  Potion.py             # Classe et fonctions pour les potions
  Salle.py              # Classe et fonctions pour les salles
  Stats.py              # Classe et fonctions pour les statistiques
```

</div>

<div id="dev">

## Développeurs 

- Emma Morgenstern 
- Milan Martz
- Paolo Atzeni

</div>