













matrix = [
    # 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 0
    [-1, 99, 99, 99, 99, -1, 99, 99, 99, 99, -1],  # 1
    [-1, 99, -1, -1, 99, -1, 99, -1, -1, 99, -1],  # 2
    [-1, 99, -1, -1, 99, 99, 99, -1, -1, 99, -1],  # 3
    [-1, 99, -1, -1, -1, -1, -1, -1, -1, 99, -1],  # 4
    [-1, 99, -1, 99, 99, 99, 99, 99, -1, 99, -1],  # 5
    [-1, 99, -1, 99, -1, -1, -1, 99, -1, 99, -1],  # 6
    [-1, 99, -1, 99, 99, 99, 99, 99, -1, 99, -1],  # 7
    [-1, 99, -1, 99, -1, 99, -1, -1, -1, 99, -1],  # 8
    [-1, 99, -1, 99, -1, 99, -1, -1, -1, 99, -1],  # 9
    [-1, 99, -1, 99, -1, 99, -1, -1, -1, 99, -1],  # 10
    [-1, 99, -1, 99, -1, 99, 99, 99, -1, 99, -1],  # 11
    [-1, 99, -1, 99, -1, -1, -1, 99, -1, 99, -1],  # 12
    [-1, 99, 99, 99, 99, 99, -1, 99, 99, 99, -1],  # 13
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 14
]





# position_defini
w = 9
v = 13

# position_initial
x = 1
y = 1

direction = 0

while not (x == w and  y == v) :
    if direction == 0 :
        if matrix [y][x-1] == 99 :
            x = x - 1
            direction = 1
            
        
            
        
            
        
        elif   matrix [y-1][x] == 99 :
            y = y - 1
             
           
            
        
        
        
        elif   matrix [y][x+1] == 99 :
            x = x + 1
            direction = 3
            
        
        
        
        else :
            direction = 1
            
        
        
    elif direction == 1 :
        
        if matrix [y+1][x] == 99 :
            y = y + 1
            direction = 2
            
        
        elif   matrix[y][x-1] == 99 :
            x = x - 1
            
        
        
        
        
        elif   matrix [y-1][x] == 99 :
            y = y - 1
            direction = 0
        
        
        
        
        else :
            direction = 2     
        
        
        
    
            
        
    
    
    elif direction == 2 :
        
        if matrix [y][x+1] == 99 :
            x = x + 1
            direction = 3
            
        
        elif   matrix [y+1][x] == 99 :
            y = y + 1
            
        
        
        
        elif   matrix [y][x-1] == 99 :
            x = x - 1
            direction = 1
        
        
        
        else :
            direction = 3
    


   
    
        
        
    elif direction == 3 :
        
        if matrix [y-1][x] == 99 :
            y = y - 1
            direction = 0
            
        
        elif   matrix [y][x+1] == 99 :
            x = x + 1
            
        
        
        
        
        elif   matrix [y+1][x] == 99 :
            y = y + 1
            direction = 2
        
        
        
        
        else :
            direction = 0
    
    
    print(y , x, direction)      
  
