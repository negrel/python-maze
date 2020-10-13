#!/usr/bin/env python

import solution
import sys
import time
import os
import resolveur
import utils
import deplacement


# Fonction pour afficher l'aide en cas d'erreur sur l'appel du script
def help_app():
    print("Le script app.py prend deux arguments :")
    print(" - Le type d'execution :")
    print(
        "     - play  -> Vous rentrez les déplacements et le minotaure les effectue."
    )
    print(
        "     - solve -> Le minotaure résoud le labyrinthe et vous retourne ses déplacements"
    )
    print(" - Le fichier .csv du labyrinthe")
    print("ex: app.py play ./exemple/exemple1.csv")


def cli(grille):
    start = [1, 1]
    end = [len(grille) - 2, len(grille[0]) - 2]

    utils.print_maze(grille, start)
    print()

    while True:
        ordres = ""
        # On demande à l'utilisateur de rentrer les ordres.
        try:
            ordres = input(f"Entrer les directions pour finir le labyrinthe: ")
        # CTRL-D on quitte le programme.
        except EOFError:
            break

        # Si on a pas gagner on affiche l'erreur retourner.
        gagner, err = solution.verifie(grille, start, end, ordres)
        if not gagner:
            print(f"Erreur: {err} (ctrl-D pour quitter)")

        else:
            print("Vous avez gagné, félicitations.")
            break


# S'il y a moins de deux argument utilisateur, on affiche l'aide et on quitte
# (Le premier argument est le nom du script)
if (len(sys.argv) < 3):
    help_app()
    exit()

# On vérifie que le fichier passé en argument existe, sinon on quitte
filename = sys.argv[2]
if not os.path.exists(filename):
    print("Le fichier '" + filename + "' n'existe pas.")
    exit()

# S'il existe, on regarde ce que l'utilisateur veut faire et on l'envoit
# sur la bonne fonction
maze = utils.loadcsv(filename)
if (sys.argv[1] == 'play'):
    cli(maze)
elif (sys.argv[1] == 'solve'):
    chemin = resolveur.mur_gauche(maze)
    directions = deplacement.analyse_chemin(chemin)
    print(f"Le minautore a suivis le chemin suivant: \n{directions}")
else:
    print("Play ou Solve en argument")
