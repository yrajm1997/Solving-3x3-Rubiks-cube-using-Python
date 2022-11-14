
def right(cube, clockwise=True):
    cub = cube.copy()
    
    l1 = cub[3, 6:9].copy()
    l2 = cub[4, 6:9].copy()
    l3 = cub[5, 6:9].copy()

    if clockwise==True:
        temp = cube[0:3,5].copy()
        cub[0:3,5] = cube[3:6, 5]
        cub[3:6, 5] = cube[6:, 5]
        cub[6:, 5] = cube[3:6, 9][::-1]
        cub[3:6, 9] = temp[::-1]
        
        cub[3:6, 8] = l1
        cub[3:6, 7] = l2
        cub[3:6, 6] = l3
        
    else:
        temp = cube[0:3,5].copy()
        cub[0:3,5] = cube[3:6, 9][::-1]
        cub[3:6, 9] = cube[-3:, 5][::-1]
        cub[-3:, 5] = cube[3:6, 5]
        cub[3:6, 5] = temp
        
        cub[5:2:-1, 6] = l1
        cub[5:2:-1, 7] = l2
        cub[5:2:-1, 8] = l3
    
    return cub


def left(cube, clockwise=True):
    cub = cube.copy()
    l1 = cub[3, 0:3].copy()
    l2 = cub[4, 0:3].copy()
    l3 = cub[5, 0:3].copy()
    
    if clockwise==True:
        temp = cub[0:3, 3].copy()
        cub[0:3, 3] = cub[3:6, -1][::-1]
        cub[3:6, -1] = cub[6:, 3][::-1]
        cub[6:, 3] = cub[3:6, 3]
        cub[3:6, 3] = temp
        
        cub[3:6, 2] = l1
        cub[3:6, 1] = l2
        cub[3:6, 0] = l3
        
    else:
        temp = cub[0:3, 3].copy()
        cub[0:3, 3] = cub[3:6, 3]
        cub[3:6, 3] = cub[6:, 3]
        cub[6:, 3] = cub[3:6, -1][::-1]
        cub[3:6, -1] = temp[::-1]
        
        cub[5:2:-1, 0] = l1
        cub[5:2:-1, 1] = l2
        cub[5:2:-1, 2] = l3
    
    return cub


def top(cube, clockwise=True):
    cub = cube.copy()
    
    l1 = cub[3, 3:6].copy()
    l2 = cub[4, 3:6].copy()
    l3 = cub[5, 3:6].copy()
    
    if clockwise==True:
        temp = cub[3:6, 2].copy()
        cub[3:6, 2] = cub[6, 3:6]
        cub[6, 3:6] = cub[3:6, 6][::-1]
        cub[3:6, 6] = cub[2, 3:6]
        cub[2, 3:6] = temp[::-1]
        
        cub[3:6, 5] = l1
        cub[3:6, 4] = l2
        cub[3:6, 3] = l3
        
    else:
        temp = cub[3:6, 2].copy()
        cub[3:6, 2] = cub[2, 3:6][::-1]
        cub[2, 3:6] = cub[3:6, 6]
        cub[3:6, 6] = cub[6, 3:6][::-1]
        cub[6, 3:6] = temp
        
        cub[5:2:-1, 3] = l1
        cub[5:2:-1, 4] = l2
        cub[5:2:-1, 5] = l3
    
    return cub


def bottom(cube, clockwise= True):
    cub = cube.copy()
    
    l1 = cub[3, 9:].copy()
    l2 = cub[4, 9:].copy()
    l3 = cub[5, 9:].copy()
    
    if clockwise==True:
        temp = cub[3:6, 0].copy()
        cub[3:6, 0] = cub[-1, 3:6]
        cub[-1, 3:6] = cub[3:6, 8][::-1]
        cub[3:6, 8] = cub[0, 3:6]
        cub[0, 3:6] = temp[::-1]
        
        cub[5:2:-1, 9] = l1
        cub[5:2:-1, 10] = l2
        cub[5:2:-1, 11] = l3
        
    else:
        temp = cub[3:6, 0].copy()
        cub[3:6, 0] = cub[0, 3:6][::-1]
        cub[0, 3:6] = cub[3:6, 8]
        cub[3:6, 8] = cub[-1, 3:6][::-1]
        cub[-1, 3:6] = temp
        
        cub[3:6, 11] = l1
        cub[3:6, 10] = l2
        cub[3:6, 9] = l3

    return cub


def front(cube, clockwise=True):
    cub = cube.copy()
    
    l1 = cub[-3, 3:6].copy()
    l2 = cub[-2, 3:6].copy()
    l3 = cub[-1, 3:6].copy()
    
    if clockwise==True:
        temp = cub[5, 3:6].copy()
        cub[5, 3:6] = cub[5, 0:3]
        cub[5, 0:3] = cub[5, -3:]
        cub[5, -3:] = cub[5, 6:9]
        cub[5, 6:9] = temp
        
        cub[-3:, 5] = l1
        cub[-3:, 4] = l2
        cub[-3:, 3] = l3
        
    else:
        temp = cub[5, 3:6].copy()
        cub[5, 3:6] = cub[5, 6:9]
        cub[5, 6:9] = cub[5, -3:]
        cub[5, -3:] = cub[5, 0:3]
        cub[5, 0:3] = temp
        
        cub[-1:-4:-1, 3] = l1
        cub[-1:-4:-1, 4] = l2
        cub[-1:-4:-1, 5] = l3

    return cub


def back(cube, clockwise=True):
    cub = cube.copy()
    
    l1 = cub[0, 3:6].copy()
    l2 = cub[1, 3:6].copy()
    l3 = cub[2, 3:6].copy()
    
    if clockwise==True:
        temp = cub[3, 3:6].copy()
        cub[3, 3:6] = cub[3, 0:3]
        cub[3, 0:3] = cub[3, -3:]
        cub[3, -3:] = cub[3, 6:9]
        cub[3, 6:9] = temp
        
        cub[0:3, 3] = l1[::-1]
        cub[0:3, 4] = l2[::-1]
        cub[0:3, 5] = l3[::-1]
        
    else:
        temp = cub[3, 3:6].copy()
        cub[3, 3:6] = cub[3, 6:9]
        cub[3, 6:9] = cub[3, -3:]
        cub[3, -3:] = cub[3, 0:3]
        cub[3, 0:3] = temp
        
        cub[0:3, 5] = l1
        cub[0:3, 4] = l2
        cub[0:3, 3] = l3

    return cub

