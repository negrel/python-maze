from algo_gauche import *
import csv1
import time
import os
clear = lambda: os.system('clear')

mino_pos = [1, 1]
mino_orientation = 0
laby = csv1.readcsv("./exemple/exemple1.csv")

moves = ''
while(mino_pos[0] != len(laby[0])-2 or mino_pos[1] != len(laby)-2):
    clear()
    csv1.printcsv(laby, mino_pos)
    mino_pos, mino_orientation, m = bougerMinotaure(laby, mino_pos, mino_orientation)
    moves += m
    time.sleep(0.2)
print(moves)