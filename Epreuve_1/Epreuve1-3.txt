#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:42:08 2020

@author: vivien
"""
#    y-1
#x-1    x+1
#    y+1

def CreationChaine(Tab,x,y,ValeurPosition):
#G : tourner à gauche
#D : tourner à droite
#T : aller tout droit (1case)
    Tab[y][x]=ValeurPosition
    ChaineCaractere = []

# Si y+1 est plus grande que ValeurPosition
        if (Tab[y+1][x]>ValeurPosition):
            CreationChaine (ChaineCaractere.append(D))
        
# Si y-1 est plus grande que ValeurPosition
        if (Tab[y-1][x]>ValeurPosition):
        	CreationChaine (ChaineCaractere.append(G))
            
# Si x+1 est plus grande que ValeurPosition
        if (Tab[y][x+1]>ValeurPosition):
    	   	CreationChaine (ChaineCaractere.append(T))
	

	


