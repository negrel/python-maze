#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:42:08 2020
@author: vivien
"""
#        T
#       y-1
#G  x-1    x+1 D
#       y+1
#        T

def CreationChaine(Tab,x,y,Position): # La fontion parcous le tableau et ajoute les caractères.
#G : tourner à gauche
#D : tourner à droite
#T : aller tout droit (1case)

    Position = Tab[y][x]
    ChaineCaractere = []
    
    # Si y-1 est plus grande que Position
    if (int(Tab[y-1][x]>Position)):
        CreationChaine(Position == [y-1][x])
        chain = "T"
        CreationChaine(ChaineCaractere.append(chain))
        CreationChaine()
        
    # Si y+1 est plus grande que Position
    if (int(Tab[y+1][x]>Position)):
        CreationChaine(Position == [y+1][x])
        chain = "T"
        CreationChaine(ChaineCaractere.append(chain))
        CreationChaine()

    # Si x-1 est plus grande que Position
    if (int(Tab[y][x-1]>Position)):
        CreationChaine(Position == [y][x-1])
        chain = "G"
        CreationChaine(ChaineCaractere.append(chain))
        CreationChaine()
            
    # Si x+1 est plus grande que Position
    if (int(Tab[y][x+1]>Position)):
        CreationChaine(Position == [y][x+1])
        chain = "D"
        CreationChaine(ChaineCaractere.append(chain))
        CreationChaine()
        
    return Tab