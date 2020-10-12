#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:42:08 2020
@author: vivien
"""
#     T
#    y-1
#G x-1    x+1 D
#    y+1
#     T

def CreationChaine(Tab,x,y,ValeurPosition):
#G : tourner à gauche
#D : tourner à droite
#T : aller tout droit (1case)
    Tab[y][x]=ValeurPosition
    ChaineCaractere = []

    # Si y-1 est plus grande que ValeurPosition
    if (Tab[y-1][x]>ValeurPosition):
        ValeurPosition = [y-1][x]
        chain = "T"
        CreationChaine(ChaineCaractere.append(chain))
        CreationChaine()
        
    # Si y+1 est plus grande que ValeurPosition
    if (Tab[y+1][x]>ValeurPosition):
        ValeurPosition = [y+1][x]
        chain = "T"
        CreationChaine(ChaineCaractere.append(chain))
        CreationChaine()
        
    # Si x-1 est plus grande que ValeurPosition
    if (Tab[y][x-1]>ValeurPosition):
        chain = "G"
        CreationChaine(ChaineCaractere.append(chain))
        CreationChaine()
            
    # Si x+1 est plus grande que ValeurPosition
    if (Tab[y][x+1]>ValeurPosition):
        chain = "D"
        CreationChaine(ChaineCaractere.append(chain))
        CreationChaine()