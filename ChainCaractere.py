#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:42:08 2020
@author: vivien
"""
#         'T'
#         y-1
# 'G' x-1       x+1 - 'D'
#         y+1
#         'T'

# La fontion parcous le tableau et ajoute les caractères en fonction de l'endroit ou se situe le minautore.
def CreationChaine(Tab,x,y,Position): 
#G : tourner à gauche
#D : tourner à droite
#T : aller tout droit (1case)
    Position = Tab[y][x]
    ChaineCaractere = []
    
    # Si y-1 est plus grande que Position
    if (int(Tab[y-1][x]>Position)):
        Position == [y-1][x]
        ChaineCaractere.append('T')
        
    # Si y+1 est plus grande que Position
    if (int(Tab[y+1][x]>Position)):
        Position == [y+1][x]
        ChaineCaractere.append('T')

    # Si x-1 est plus grande que Position
    if (int(Tab[y][x-1]>Position)):
        Position == [y][x-1]
        ChaineCaractere.append('G')
            
    # Si x+1 est plus grande que Position
    if (int(Tab[y][x+1]>Position)):
        Position == [y][x+1]
        ChaineCaractere.append('D')
    return ChaineCaractere


