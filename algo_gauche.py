#!/usr/bin/env python

orientations = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]

str_orientation = ['G', 'T', 'D', 'GG']

def bougerMinotaure(matrice, position, dir):
    # on parcout les cases en suivant l'orientation G, T, D, GG
    for i in [-1, 0, 1, 2]:
        # On récupère les coordonnées de la case que l'on check
        offset_x = position[0] + orientations[(dir + i) % 4][0]
        offset_y = position[1] + orientations[(dir + i) % 4][1]
        # Si la case est vide, on return la nouvelle position du minotaure,
        # ainsi que sa nouvelle direction, et ses mouvements effectués
        if(matrice[offset_y][offset_x] == 99):
            str_move = str_orientation[i+1] + ('T' if i != 0 else '')
            return ([offset_x, offset_y], (dir + i) % 4, str_move)
        # Sinon, on continue de tourner dans la for jusqu'à trouver une case vide.
            
