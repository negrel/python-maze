# Projet d'intégrationer 1 année "labyrinthe"

## Sommaire:
- Lancer le programme
- Epreuve 1
- Explication
    - Algorithme du mur gauche
- Auteurs
- Professeurs

## Lancer le programme:

```bash
# Installation des dépendances
pip install -r requirements.txt

# Lancement du programme
python ./app.py
```

## Epreuve 1 :

Traverser un labyrinthe Un labyrinthe est représenté par une matrice m×n dans laquelle les cases remplies de 99 
sont accessibles, celles remplies d'un -1 ne le sont pas. Les bords sont intégralement 
remplis avec des -1 pour éviter les problèmes de débordement. 

Le minotaure pénètre dans le labyrinthe par l’un des coins et ressort par un autre. 
On suppose que le minotaure ne peut se déplacer que dans 4 directions : haut, bas, gauche, droite. 
Dans notre exemple il entre par la case [1;1] et doit sortir par la case [m-2;n-2]. Rendu le 13/10 à 12h max via moodle 
Projet d'intégration informatique MSIR1A 2020 Milles

S1 Liste des programmes à fournir: 
- Charger un fichier CSV et l’afficher
    - Implémenté dans `utils.py` (Florian MARTIN, Eliot MARECHAL)

- Algo “mur gauche”
    - Il y a 3 implémentations différente dans `resolveur.py` (Chrisophe BALLAIRE, Eliot MARECHAL, Alexandre NEGREL)
- Programme qui affiche la suite des directions. Vous devez produire une chaîne d’ordres qui sera ensuite lue au minotaure pour se déplacer. Par exemple, G pour tourner dans la cellule à gauche, D pour tourner dans la cellule à droite et T pour aller tout droit. 
Par exemple : TTGTDTTDTTTG.
    - Implémenté dans `déplacement.py` (Romain VIVIEN)
- Savoir lire un ensemble d’ordre sous le format ci dessus, en ligne de commande, et l’exécuter dans le labyrinthe en affichant le déplacement effectif et les erreurs si il y en a.
    - Implémenté dans `solution.py` (Alexandre NEGREL)
- Intégration
    - Implémenté dans `app.py` (Chrisophe BALLAIRE, Eliot MARECHAL, Alexandre NEGREL, Romain VIVIEN)

## Explication
### Algorithme du `mur gauche`:
L'algorithme du mur gauche consiste à suivre le mur d'un labyrinthe jusqu'a atteindre la sortie.

```python
HAUT: int    <- 0
DROITE: int  <- 1
BAS: int     <- 2
GAUCHE: int  <- 3

directions [4][2]int <- [
  [-1, 0], # HAUT
  [0, 1], # DROITE
  [1, 0], # BAS
  [0, -1], # GAUCHE
]

function mur_gauche(grille: [][]int)
    # On définit le point de départ et de fin du labyrinthe
    start: [2]int <- [1, 1] # En haut à gauche
    end: [2]int <- [len(grille) - 2, len(grille[0]) - 2] # En bas à droite

    # Liste des cases par lequel ils passent
    chemin: []int <- [start]

    # Position et direction du minautore
    position: [2]int <- start
    direction: [2]int <- directions[DROITE]

    while position =/= end
        # On essaie de tourner à gauche
        nouvelle_direction: [2]int <- tourner(direction, droite=False)

        x: int
        y: int
        y, x <- avancer(position, nouvelle_direction)

        # On peut tourner a gauche
        if grille[y][x] = 99
            direction <- nouvelle_direction
            position <- [y, x]

            # On ajoute la case au chemin
            chemin.append(position)

        # On ne peut pas tourner à gauche
        else
            # On tourne à droite
            direction <- tourner(direction, droite=True)

    # On retourne le chemin emprunté
    return chemin


# avance prend une position et une direction et avance une fois
# dans la direction
function avancer(position: [2]int, direction: [2]int)
    y <- position[0] + direction[0]
    x <- position[1] + direction[1]

    return [y, x]

# tourner prend une direction en paramètre et retourne une direction
# de 90° vers la droite ou la gauche.
function tourner(dir_actuel: [2]int, droite: boolean)
    # On inverse le signe si necessaire
    if droite and droite[1] = 0:
        droite[0] <- -1
    elif not droite and droite[0] = 0:
        droite[1] <- -1

    # On inverse l'index Y et X
    x <- dir_actuel[0]
    y <- dir_actuel[1]

    return [y, x]
```

## Auteurs 
 - Romain VIVIEN
 - Alexandre NEGREL
 - Christophe BALLAIRE
 - Eliot MARECHAL 
 - Florian MARTIN 

## Professeurs
 - Gilles MATEU
 - Eric SALVAT
 - Blaise MADELINE 
 - Ahmed RHARMAOUI
