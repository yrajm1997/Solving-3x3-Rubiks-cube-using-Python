from rotate_side import right, left, top, bottom, front, back

def t_perm(cube):
    
    ''' [R U R' U'] R' F R2 U' R' U' [R U R' F'] '''
    
    cub = cube.copy()
    
    cub = right(cub)
    cub = top(cub)
    cub = right(cub, False)
    cub = top(cub, False)
    cub = right(cub, False)
    cub = front(cub)
    cub = right(right(cub))
    cub = top(cub, False)
    cub = right(cub, False)
    cub = top(cub, False)
    cub = right(cub)
    cub = top(cub)
    cub = right(cub, False)
    cub = front(cub, False)
    
    return cub


def y_perm(cube):
    
    ''' (R U' R' U') R U R' F' (R U R' U') R' F R  '''
    
    cub = cube.copy()
    
    cub = right(cub)
    cub = top(cub, False)
    cub = right(cub, False)
    cub = top(cub, False)
    cub = right(cub)
    cub = top(cub)
    cub = right(cub, False)
    cub = front(cub, False)
    cub = right(cub)
    cub = top(cub)
    cub = right(cub, False)
    cub = top(cub, False)
    cub = right(cub, False)
    cub = front(cub)
    cub = right(cub)
    
    return cub
