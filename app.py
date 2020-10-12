#!/usr/bin/env python

import csv1
import solution
import sys
import algo_gauche
import time
import os
clear = lambda: os.system('clear')

# Fonction pour afficher l'aide en cas d'erreur sur l'appel du script
def help_app():
    print("Le script app.py prend deux arguments :");
    print(" - Le type d'execution :")
    print("     - play  -> Vous rentrez les déplacements et le minotaure les effectue.")
    print("     - solve -> Le minotaure résoud le labyrinthe et vous retourne ses déplacements")
    print(" - Le fichier .csv du labyrinthe")
    print("ex: app.py play ./exemple/exemple1.csv")

def cli(grille):
    start = [1, 1]
    end = [len(grille)-2, len(grille[0])-2]

    csv1.printcsv(grille, start)
    print()

    while True:
        ordres = ""
        # On demande à l'utilisateur de rentrer les ordres.
        try:
            ordres = input(
            f"Entrer les directions pour finir le labyrinthe: ")
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

def autoFind(grille):
    mino_pos = [1, 1]
    mino_orientation = 0
    end = [len(grille[0])-2, len(grille)-2]
    moves = ''

    while(mino_pos[0] != end[0] or mino_pos[1] != end[1]):
        clear()
        csv1.printcsv(laby, mino_pos)
        mino_pos, mino_orientation, m = algo_gauche.bougerMinotaure(laby, mino_pos, mino_orientation)
        moves += m
        time.sleep(0.2)
    csv1.printcsv(laby, mino_pos)
    print("Labyrinthe résolu en "+ str(len(moves)) +" coups.")
    print("Liste des coups :")
    print(moves)


if(len(sys.argv) < 3):
    help_app()
    exit()

filename = sys.argv[2]
if not os.path.exists(filename):
    print("Le fichier '"+ filename +"' n'existe pas.")
    exit()

laby = csv1.readcsv(filename)
if(sys.argv[1] == 'play'):
    cli(laby)
elif(sys.argv[1] == 'solve'):
    autoFind(laby)
else:
    print("Play ou Solve en argument")
