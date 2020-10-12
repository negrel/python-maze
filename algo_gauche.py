#!/usr/bin/env python

orientations = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
]

str_orientation = ['G', 'T', 'D', 'GG']

def bougerMinotaure(matrice, position, dir):
    for i in [-1, 0, 1, 2]:
        offset_x = position[0] + orientations[(dir + i) % 4][0]
        offset_y = position[1] + orientations[(dir + i) % 4][1]
        if(matrice[offset_y][offset_x] == 99):
            str_move = str_orientation[i+1] + ('T' if i != 0 else '')
            return ([offset_x, offset_y], (dir + i) % 4, str_move)
            
