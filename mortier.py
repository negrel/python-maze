#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame 
import math

fenetre = pygame.display.set_mode = ((700, 700))
pos_mortier = [0,700]
pos_cible = [550, 250]


g = 9.81

def ditance_tir(obus):
    return(obus.v0 * obus.v0 * math.sin(2.0 * obus.alpha)) / g
    
    

class Obus:
    def __init__(self):
        self.v0 = 0.0
        self.alpha = 0.0
        
# definir l'obus!!   
        
class cible:
    def __init__(self):
        self.dc = 0.0
        self.rc = 0.0
        
# definir la cible!!
        
        
def angle(x1, x1, y1, y2):
    return math.atan((y2-y1)/(x2-x1))
        
def trajectoire(x, y):
    return x*(math.tan(alpha))-(g*x*x)/(2*v0*(math.cos(alpha)*v0*math.cos(alpha)))


        
        
TOUCHE = 0
COURT = -1
LONG = 1



class resultat_tire:
    def __init__(self):
        self.dist = 0.0
        self.rtir = 0
        

    def tire(obus, cible, resultat):
        resultat.dist = distanceTir(obus)
        if resultat.dist < cible.dc - cible.rc:
            resultat.rtir = COURT
        elif resultat.dist > cible.dc + cible.rc:
            resultat.rtir = LONG
        else:
            resultat.rtir = TOUCHE
            
            
     def affichage_resultat(resultat):
         print("L'obus est tombé à ", resltat.dist, " metres")
         if resultat.rtir == COURT:
             print("Cible ratée, TROP COURT !")
         elif resultat.rtir == LONG:
             print("Cible ratee, TROP LONG  !")
         elif resultat.rtir == TOUCHE:
             print("CIBLE TOUCHEE !!!")
     
            
        
        
        
        
        
    
    
    