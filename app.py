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
    # Définitino des variables de base
    mino_pos = [1, 1]
    mino_orientation = 0
    end = [len(grille[0])-2, len(grille)-2]
    moves = ''

    # Tant que le mino n'est pas sur la case d'arrivée
    while(mino_pos[0] != end[0] or mino_pos[1] != end[1]):
        # On clear la console et on affiche la labyrinthe
        clear()
        csv1.printcsv(laby, mino_pos)
        # On bouge le minotaure est on récupère ses nouvelles informations
        mino_pos, mino_orientation, m = algo_gauche.bougerMinotaure(laby, mino_pos, mino_orientation)
        # On met à jour les mouvements effectués
        moves += m
        time.sleep(0.2)
    # On réaffiche une dernière fois pour voir le minot aure sur l'arrivée
    csv1.printcsv(laby, mino_pos)
    print("Labyrinthe résolu en "+ str(len(moves)) +" coups.")
    print("Liste des coups :")
    print(moves)

# S'il y a moins de deux argument utilisateur, on affiche l'aide et on quitte
# (Le premier argument est le nom du script)
if(len(sys.argv) < 3):
    help_app()
    exit()

# On vérifie que le fichier passé en argument existe, sinon on quitte
filename = sys.argv[2]
if not os.path.exists(filename):
    print("Le fichier '"+ filename +"' n'existe pas.")
    exit()

# S'il existe, on regarde ce que l'utilisateur veut faire et on l'envoit
# sur la bonne fonction
laby = csv1.readcsv(filename)
if(sys.argv[1] == 'play'):
    cli(laby)
elif(sys.argv[1] == 'solve'):
    autoFind(laby)
else:
    print("Play ou Solve en argument")
