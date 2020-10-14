#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame
#import time
import turtle


pygame.init()


#taille_police = 12
#taille_police2 = 17
#taille_police3 = 15

#POLICE = ('Arial', taille_police, 'normal')
#POLICE2 = ('Arial', taille_police2, 'normal')
#POLICE3 = ('Arial', taille_police3, 'normal')

police1 = pygame.font.SysFont("comicsansms", 12, True)
police2 = pygame.font.SysFont("comicsansms", 17, True)
police3 = pygame.font.SysFont("comicsansms", 15, True)

fenetre = pygame.display.set_mode((200, 60))
# creer str qui affiche le temps
def temps(minutes,secondes):
    
    turtle.write(temps, police1, police2, police3)

    turtle.mainloop()

    if len(str(minutes)) > 1:
        m = str(minutes)
    else:
        m = "0" + str(minutes)

    if len(str(secondes)) > 1:
        s = str(secondes)
    else:
        s = "0" + str(secondes)

    return m + ":" + s

# creer le chrono
def chrono(temps_de_depart):
    minutes = 0
    secondes = 0
    temps_depart = 0
    temps_actuelle = temps.temps() - temps_depart
    if temps_actuelle > 60:
        while True:
            
     
            if temps_actuelle - 60 > 0:
                minutes += 1
                temps_actuelle -= 60
            else:
                secondes += int(temps_actuelle)
                break
            
        
    return [police1.render(temps(minutes, secondes), True, (0, 0, 0), (255, 255, 255)), temps(minutes, secondes)] 

pygame.display.flip()










