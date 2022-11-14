from rotate_side import right, left, top, bottom, front, back
from algorithms import t_perm, y_perm

def edges(cube):
    
    cub = cube.copy()
    stps = []
    tperm_stps = ["R","U","R'", "U'", "R'", "F", "R", "R", "U'", "R'", "U'", "R", "U", "R'", "F'"]
    
    if (cub[0, 4] == 'G' and  cub[3, -2] == 'Y') and (cub[4, -4] == 'O' and  cub[4, -3] == 'Y') and (cub[-1, 4] == 'B' and  cub[-4, -2] == 'Y') and (cub[4, 0] == 'R' and  cub[4, -1] == 'Y') and (cub[3, 7] == 'O' and  cub[1, 5] == 'G') and (cub[-2, 5] == 'B' and  cub[-4, 7] == 'O') and (cub[5, 1] == 'R' and  cub[-2, 3] == 'B') and (cub[1, 3] == 'G' and  cub[3, 1] == 'R') and (cub[5, 4] == 'W' and  cub[6, 4] == 'B') and (cub[3, 4] == 'W' and  cub[2, 4] == 'G') and (cub[4, 5] == 'W' and cub[4, 6] == 'O') and (cub[4, 2] == 'R' and cub[4, 3] == 'W'):
        return cub, stps
    
    else: 
        if cub[4, 5] == 'B' and cub[4, 6] == 'R':             ###############
            cub = left(t_perm(left(cub, False)))
            stps += ["L'"] + tperm_stps + ["L"]
        
        elif cub[4, 5] == 'R' and cub[4, 6] == 'B':          ################
            cub = top(front(top(t_perm(top(front(top(cub, False)))), False), False))
            stps += ["U'", "F", "U"] + tperm_stps + ["U'", "F'", "U"]
        
        elif cub[4, 5] == 'G' and cub[4, 6] == 'R':           ###############
            cub = left(t_perm(left(cub)), False)
            stps += ["L"] + tperm_stps + ["L'"]
        
        elif cub[4, 5] == 'R' and cub[4, 6] == 'G':           ##############
            cub = top(back(top(t_perm(top(back(top(cub)), False))), False), False)
            stps += ["U", "B", "U'"] + tperm_stps + ["U", "B'", "U'"]
        
        elif cub[4, 5] == 'O' and cub[4, 6] == 'G':           ##############
            cub = top(back(top(t_perm(top(back(top(cub), False), False)))), False)
            stps += ["U", "B'", "U'"] + tperm_stps + ["U", "B", "U'"]
        
        elif cub[4, 5] == 'G' and cub[4, 6] == 'O':           ##############
            cub = top(top(right(top(top(t_perm(top(top(right(top(top(cub)), False)))))))))
            stps += ["U", "U", "R'", "U", "U"] + tperm_stps + ["U", "U", "R", "U", "U"]
        
        elif cub[4, 5] == 'O' and cub[4, 6] == 'B':           ##############
            cub = top(front(top(t_perm(top(front(top(cub, False), False))), False)))
            stps += ["U'", "F'", "U"] + tperm_stps + ["U'", "F", "U"]
        
        elif cub[4, 5] == 'B' and cub[4, 6] == 'O':           ##############
            cub = top(top(right(top(top(t_perm(top(top(right(top(top(cub)))))))), False)))
            stps += ["U", "U", "R", "U", "U"] + tperm_stps + ["U", "U", "R'", "U", "U"]
            
        elif cub[4, 5] == 'Y' and cub[4, 6] == 'R':           ##############
            cub = left(left(t_perm(left(left(cub)))))
            stps += ["L", "L"] + tperm_stps + ["L", "L"]
        
        elif cub[4, 5] == 'Y' and cub[4, 6] == 'G':           ##############
            cub = bottom(left(left(t_perm(left(left(bottom(cub, False)))))))
            stps += ["D'", "L", "L"] + tperm_stps + ["L", "L", "D"]
        
        elif cub[4, 5] == 'Y' and cub[4, 6] == 'O':           ##############
            cub = bottom(bottom(left(left(t_perm(left(left(bottom(bottom(cub)))))))))
            stps += ["D", "D", "L", "L"] + tperm_stps + ["L", "L", "D", "D"]
        
        elif cub[4, 5] == 'Y' and cub[4, 6] == 'B':           ##############
            cub = bottom(left(left(t_perm(left(left(bottom(cub)))))), False)
            stps += ["D", "L", "L"] + tperm_stps + ["L", "L", "D'"]
        
        elif cub[4, 5] == 'R' and cub[4, 6] == 'Y':           ###############
            cub = left(top(back(top(t_perm(top(back(top(left(cub))), False))), False), False), False)
            stps += ["L", "U", "B", "U'"] + tperm_stps + ["U", "B'", "U'", "L'"]
            
        elif cub[4, 5] == 'G' and cub[4, 6] == 'Y':           ################
            cub = bottom(left(top(back(top(t_perm(top(back(top(left(bottom(cub, False)))), False))), False), False), False))
            stps += ["D'", "L", "U", "B", "U'"] + tperm_stps + ["U", "B'", "U'", "L'", "D"]
            
        elif cub[4, 5] == 'O' and cub[4, 6] == 'Y':           ###############
            cub = bottom(bottom(left(top(back(top(t_perm(top(back(top(left(bottom(bottom(cub))))), False))), False), False), False)))
            stps += ["D", "D", "L", "U", "B", "U'"] + tperm_stps + ["U", "B'", "U'", "L'", "D", "D"]
            
        elif cub[4, 5] == 'B' and cub[4, 6] == 'Y':           #################
            cub = bottom(left(top(back(top(t_perm(top(back(top(left(bottom(cub)))), False))), False), False), False), False)
            stps += ["D", "L", "U", "B", "U'"] + tperm_stps + ["U", "B'", "U'", "L'", "D'"]
            
        elif cub[4, 5] == 'R' and cub[4, 6] == 'W':           #################
            cub = left(top(back(top(t_perm(top(back(top(left(cub, False))), False))), False), False))
            stps += ["L'", "U", "B", "U'"] + tperm_stps + ["U", "B'", "U'", "L"]
            
        elif cub[4, 5] == 'G' and cub[4, 6] == 'W':           #################
            cub = right(back(left(right(t_perm(right(left(back(right(cub, False), False)))), False), False)))
            stps += ["R'", "B'", "L", "R"] + tperm_stps + ["R'", "L'", "B", "R"]
        
        elif cub[4, 5] == 'B' and cub[4, 6] == 'W':           ##################
            cub = right(front(left(right(t_perm(right(left(front(right(cub), False), False), False))))), False)
            stps += ["R", "F'", "L'", "R'"] + tperm_stps + ["R", "L", "F", "R'"]
        
        elif cub[4, 5] == 'W' and cub[4, 6] == 'R':           ##################
            cub = t_perm(cub)
            stps += tperm_stps
        
        elif cub[4, 5] == 'W' and cub[4, 6] == 'G':           ###################
            cub = right(right(top(right(right(t_perm(right(right(top(right(right(cub)), False)))))))))
            stps += ["R", "R", "U'", "R", "R"] + tperm_stps + ["R", "R", "U", "R", "R"]
        
        elif cub[4, 5] == 'W' and cub[4, 6] == 'B':           ###################
            cub = right(right(top(right(right(t_perm(right(right(top(right(right(cub)))))))), False)))
            stps += ["R", "R", "U", "R", "R"] + tperm_stps + ["R", "R", "U'", "R", "R"]
        
        elif (cub[4, 5] == 'W' and cub[4, 6] == 'O') or (cub[4, 5] == 'O' and cub[4, 6] == 'W'):
        
            if (cub[0, 4] == 'G' and  cub[3, -2] == 'Y') == False:                  ##################
                cub = bottom(left(left(t_perm(left(left(bottom(cub, False)))))))
                stps += ["D'", "L", "L"] + tperm_stps + ["L", "L", "D"]
            
            elif (cub[4, -4] == 'O' and  cub[4, -3] == 'Y') == False:               ##################
                cub = bottom(bottom(left(left(t_perm(left(left(bottom(bottom(cub)))))))))
                stps += ["D", "D", "L", "L"] + tperm_stps + ["L", "L", "D", "D"]
                
            elif (cub[-1, 4] == 'B' and  cub[-4, -2] == 'Y') == False:             ###################
                cub = bottom(left(left(t_perm(left(left(bottom(cub)))))), False)
                stps += ["D", "L", "L"] + tperm_stps + ["L", "L", "D'"]
                
            elif (cub[4, 0] == 'R' and  cub[4, -1] == 'Y') == False:               ##################
                cub = left(left(t_perm(left(left(cub)))))
                stps += ["L", "L"] + tperm_stps + ["L", "L"]
            
            elif (cub[3, 7] == 'O' and  cub[1, 5] == 'G') == False:                ##################
                cub = top(back(top(t_perm(top(back(top(cub), False), False)))), False)
                stps += ["U", "B'", "U'"] + tperm_stps + ["U", "B", "U'"]
                    
            elif (cub[-2, 5] == 'B' and  cub[-4, 7] == 'O') == False:              ##################
                cub = top(top(right(top(top(t_perm(top(top(right(top(top(cub)))))))), False)))
                stps += ["U", "U", "R", "U", "U"] + tperm_stps + ["U", "U", "R'", "U", "U"]
                
            elif (cub[5, 1] == 'R' and  cub[-2, 3] == 'B') == False:               ##################
                cub = left(t_perm(left(cub, False)))
                stps += ["L'"] + tperm_stps + ["L"]
                
            elif (cub[1, 3] == 'G' and  cub[3, 1] == 'R') == False:                ##################
                cub = left(t_perm(left(cub)), False)
                stps += ["L"] + tperm_stps + ["L'"]
                
            elif (cub[5, 4] == 'W' and  cub[6, 4] == 'B') == False:                ##################
                cub = right(right(top(right(right(t_perm(right(right(top(right(right(cub)))))))), False)))
                stps += ["R", "R", "U", "R", "R"] + tperm_stps + ["R", "R", "U'", "R", "R"]
                
            elif (cub[3, 4] == 'W' and  cub[2, 4] == 'G') == False:               ###################
                cub = right(right(top(right(right(t_perm(right(right(top(right(right(cub)), False)))))))))
                stps += ["R", "R", "U'", "R", "R"] + tperm_stps + ["R", "R", "U", "R", "R"]
                
            elif (cub[4, 2] == 'R' and cub[4, 3] == 'W') == False:               ####################
                cub = t_perm(cub)
                stps += tperm_stps
                
            else: 
                return cub, stps
 

    return cub, stps


def corners(cube):
    
    cub = cube.copy()
    stps = []
    yperm_stps = ["R", "U'", "R'", "U'", "R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R"]
    
    if (cub[0, 5]=='G' and cub[3, 9]=='Y' and cub[3, 8]=='O') and (cub[3, 0]=='R' and cub[3, -1]=='Y' and cub[0, 3]=='G') and (cub[-1, 3]=='B' and cub[5, -1]=='Y' and cub[5, 0]=='R') and (cub[5, 8]=='O' and cub[5, 9]=='Y' and cub[-1, 5]=='B') and (cub[3, 5]=='W' and cub[2, 5]=='G' and cub[3, 6]=='O') and (cub[3, 3]=='W' and cub[3, 2]=='R' and cub[2, 3]=='G') and (cub[5, 3]=='W' and cub[6, 3]=='B' and cub[5, 2]=='R') and (cub[5, 5]=='W' and cub[5, 6]=='O' and cub[6, 5]=='B'):
        return cub, stps
    
    else: 
        if cub[3, 3]=='O' and cub[3, 2]=='Y' and cub[2, 3]=='B':             ###############
            cub = y_perm(cub)
            stps += yperm_stps
        
        elif cub[3, 3]=='B' and cub[3, 2]=='O' and cub[2, 3]=='Y':          ################
            cub = bottom(right(y_perm(right(bottom(cub, False))), False))
            stps += ["D'", "R"] + yperm_stps + ["R'", "D"]
        
        elif cub[3, 3]=='Y' and cub[3, 2]=='B' and cub[2, 3]=='O':           ###############
            cub = right(bottom(y_perm(bottom(right(cub, False))), False))
            stps += ["R'", "D"] + yperm_stps + ["D'", "R"]
        
        elif cub[3, 3]=='B' and cub[3, 2]=='Y' and cub[2, 3]=='R':           ##############
            cub = bottom(y_perm(bottom(cub, False)))
            stps += ["D'"] + yperm_stps + ["D"]
        
        elif cub[3, 3]=='Y' and cub[3, 2]=='R' and cub[2, 3]=='B':           ##############
            cub = front(y_perm(front(cub, False)))
            stps += ["F'"] + yperm_stps + ["F"]
        
        elif cub[3, 3]=='R' and cub[3, 2]=='B' and cub[2, 3]=='Y':           ##############
            cub = bottom(bottom(right(y_perm(right(bottom(bottom(cub, False), False))), False)))
            stps += ["D'", "D'", "R"] + yperm_stps + ["R'", "D", "D"]
        
        elif cub[3, 3]=='R' and cub[3, 2]=='Y' and cub[2, 3]=='G':           ##############
            cub = bottom(bottom(y_perm(bottom(bottom(cub)))))
            stps += ["D", "D"] + yperm_stps + ["D", "D"]
        
        elif cub[3, 3]=='Y' and cub[3, 2]=='G' and cub[2, 3]=='R':           ##############
            cub = bottom(front(y_perm(front(bottom(cub, False), False))))
            stps += ["D'", "F'"] + yperm_stps + ["F", "D"]
        
        elif cub[3, 3]=='G' and cub[3, 2]=='R' and cub[2, 3]=='Y':           ##############
            cub = bottom(right(y_perm(right(bottom(cub))), False), False)
            stps += ["D", "R"] + yperm_stps + ["R'", "D'"]
        
        elif cub[3, 3]=='G' and cub[3, 2]=='Y' and cub[2, 3]=='O':           ##############
            cub = bottom(y_perm(bottom(cub)), False)
            stps += ["D"] + yperm_stps + ["D'"]
        
        elif cub[3, 3]=='Y' and cub[3, 2]=='O' and cub[2, 3]=='G':           ##############
            cub = right(right(front(y_perm(front(right(right(cub)))), False)))
            stps += ["R", "R", "F"] + yperm_stps + ["F'", "R", "R"]
        
        elif cub[3, 3]=='O' and cub[3, 2]=='G' and cub[2, 3]=='Y':           ##############
            cub = right(y_perm(right(cub)), False)
            stps += ["R"] + yperm_stps + ["R'"]
        
        elif cub[3, 3]=='W' and cub[3, 2]=='O' and cub[2, 3]=='B':           ###############
            cub = front(y_perm(front(cub)), False)
            stps += ["F"] + yperm_stps + ["F'"]
        
        elif cub[3, 3]=='O' and cub[3, 2]=='B' and cub[2, 3]=='W':           ################
            cub = right(y_perm(right(cub, False)))
            stps += ["R'"] + yperm_stps + ["R"]
            
        elif cub[3, 3]=='B' and cub[3, 2]=='W' and cub[2, 3]=='O':           ###############
            cub = right(right(bottom(y_perm(bottom(right(right(cub)))), False)))
            stps += ["R", "R", "D"] + yperm_stps + ["D'", "R", "R"]
        
        elif cub[3, 3]=='W' and cub[3, 2]=='B' and cub[2, 3]=='R':           #################
            cub = front(right(y_perm(right(front(cub), False))), False)
            stps += ["F", "R'"] + yperm_stps + ["R", "F'"]
        
        elif cub[3, 3]=='B' and cub[3, 2]=='R' and cub[2, 3]=='W':           #################
            cub = front(bottom(y_perm(bottom(front(cub, False), False))))
            stps += ["F'", "D'"] + yperm_stps + ["D", "F"]
        
        elif cub[3, 3]=='R' and cub[3, 2]=='W' and cub[2, 3]=='B':           #################
            cub = front(front(y_perm(front(front(cub)))))
            stps += ["F", "F"] + yperm_stps + ["F", "F"]
        
        elif cub[3, 3]=='W' and cub[3, 2]=='G' and cub[2, 3]=='O':           ##################
            cub = right(bottom(y_perm(bottom(right(cub))), False), False)
            stps += ["R", "D"] + yperm_stps + ["D'", "R'"]
        
        elif cub[3, 3]=='G' and cub[3, 2]=='O' and cub[2, 3]=='W':           ##################
            cub = right(front(y_perm(front(right(cub, False))), False))
            stps += ["R'", "F"] + yperm_stps + ["F'", "R"]

        elif cub[3, 3]=='O' and cub[3, 2]=='W' and cub[2, 3]=='G':           ###################
            cub = right(right(y_perm(right(right(cub)))))
            stps += ["R", "R"] + yperm_stps + ["R", "R"]

        
        elif (cub[3, 3]=='G' and cub[3, 2]=='W' and cub[2, 3]=='R') or (cub[3, 3]=='R' and cub[3, 2]=='G' and cub[2, 3]=='W') or (cub[3, 3]=='W' and cub[3, 2]=='R' and cub[2, 3]=='G'):
        
            if (cub[5, 5]!='W' or cub[5, 6]!='O' or cub[6, 5]!='B'):                  ##################
                cub = front(y_perm(front(cub)), False)
                stps += ["F"] + yperm_stps + ["F'"]
            
            elif (cub[5, 3]!='W' or cub[6, 3]!='B' or cub[5, 2]!='R'):               ##################
                cub = front(front(y_perm(front(front(cub)))))
                stps += ["F", "F"] + yperm_stps + ["F", "F"]
            
            elif (cub[3, 5]!='W' or cub[2, 5]!='G' or cub[3, 6]!='O'):              ###################
                cub = right(right(y_perm(right(right(cub)))))
                stps += ["R", "R"] + yperm_stps + ["R", "R"]
            
            elif (cub[5, 8]!='O' or cub[5, 9]!='Y' or cub[-1, 5]!='B'):              ##################
                cub = y_perm(cub)
                stps += yperm_stps  
            
            elif (cub[-1, 3]!='B' or cub[5, -1]!='Y' or cub[5, 0]!='R'):                ##################
                cub = bottom(y_perm(bottom(cub, False)))
                stps += ["D'"] + yperm_stps + ["D"]
            
            elif (cub[3, 0]!='R' or cub[3, -1]!='Y' or cub[0, 3]!='G'):              ##################
                cub = right(right(y_perm(right(right(cub)))))
                stps += ["R", "R"] + yperm_stps + ["R", "R"]
            
            elif (cub[0, 5]!='G' or cub[3, 9]!='Y' or cub[3, 8]!='O'):               ##################
                cub = bottom(y_perm(bottom(cub)), False)
                stps += ["D"] + yperm_stps + ["D'"]
                        
            else: 
                return cub, stps
 

    return cub, stps

