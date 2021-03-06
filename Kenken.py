from ortools.sat.python import cp_model
n = 10
def restrictions(dificultad, model, grilla, laux, strategy):
    # Restricciones
    for i in range(n):
        # Toda fila tiene valores distintos
        model.AddAllDifferent(grilla[i])
        # Toda columna tiene valores distintos
        model.AddAllDifferent([x[i] for x in grilla])
    # Cages
    
    if dificultad == 1:
        model.Add(grilla[0][1] + grilla[1][1] == 7)
        model.Add(grilla[0][2] + grilla[0][3] + grilla[0][4] + grilla[1][3] + grilla[1][4] == 38)
        model.Add(grilla[0][5] + grilla[0][6] + grilla[1][5] + grilla[1][6] == 23)
        model.Add(grilla[0][7] + grilla[1][7] + grilla[2][7] + grilla[1][8] == 23)
        model.Add(grilla[0][8] + grilla[0][9] == 9)
        model.Add(grilla[1][2] + grilla[2][2] + grilla[2][3] == 8)
        model.Add(grilla[1][9] + grilla[2][8] + grilla[2][9] == 16)
        aux1 = model.NewIntVar(-1,1,'aux1')
        model.Add(grilla[2][1] - grilla[2][0] == aux1)
        model.AddAbsEquality(1,aux1)
        #model.Add(grilla[2][0] - grilla[2][1] == 1)
        model.Add(grilla[2][4] == 5)
        model.Add(grilla[2][5] + grilla[3][5] + grilla[3][6] == 11)
        model.Add(grilla[2][6] == 6)
        model.Add(grilla[3][0] == 8)
        model.Add(grilla[3][1] + grilla[3][2] + grilla[3][3] + grilla[3][4] == 25)
        model.Add(grilla[3][7] + grilla[3][8] + grilla[4][7] == 21)
        model.Add(grilla[3][9] == 4)
        model.Add(grilla[4][0] == 3)
        model.Add(grilla[4][1] + grilla[5][0] + grilla[5][1]  == 14)
        model.Add(grilla[4][2] == 2)
        model.Add(grilla[4][3] + grilla[4][4] + grilla[4][5] + grilla[5][5] == 28)
        model.Add(grilla[4][6] == 5)
        model.Add(grilla[4][8] + grilla[5][8] == 6)
        aux2 = model.NewIntVar(-7,7,'aux2')
        model.Add(grilla[5][9] - grilla[4][9] == aux2)
        model.AddAbsEquality(7,aux2)
        #model.Add(grilla[4][9] - grilla[5][9] == 7)
        aux3 = model.NewIntVar(-2,2,'aux3')
        model.Add(grilla[6][2] - grilla[5][2] == aux3)
        model.AddAbsEquality(2,aux3)
        #model.Add( grilla[6][2] - grilla[5][2] == 2)
        model.Add(grilla[5][3] + grilla[5][4] + grilla[6][3] == 19)
        aux4 = model.NewIntVar(-7,7,'aux4')
        model.Add(grilla[5][6] - grilla[6][6] == aux4)
        model.AddAbsEquality(7, aux4)
        #model.Add(grilla[5][6] - grilla[6][6] == 7)
        model.Add(grilla[5][7] == 3)
        model.Add(grilla[6][0] + grilla[7][0] + grilla[8][0] == 20)
        model.Add(grilla[6][1] == 6)
        model.Add(grilla[6][4] == 3)
        model.Add(grilla[6][5] + grilla[7][5] + grilla[7][6] + grilla[8][5]  == 19)
        model.Add(grilla[6][7] + grilla[6][8] == 11)
        model.Add(grilla[6][9] + grilla[7][9] == 14)
        model.Add(grilla[7][1] + grilla[7][2] + grilla[8][1] + grilla[8][2] == 19)
        model.Add(grilla[7][3] == 2)
        model.Add(grilla[8][3] + grilla[8][4] + grilla[7][4] == 16)
        model.Add(grilla[7][7] + grilla[7][8] + grilla[8][6]  + grilla[8][7] == 24)
        aux5 = model.NewIntVar(-7,7,'aux5')
        model.Add(grilla[8][9] - grilla[8][8] == aux5)
        model.AddAbsEquality(7, aux5)
        #model.Add(grilla[8][9] - grilla[8][8] == 7)
        model.Add(grilla[9][0] == 1)
        aux6 = model.NewIntVar(-2, 2, 'aux6')
        model.Add(grilla[9][2] - grilla[9][1] == aux6)
        model.AddAbsEquality(2,aux6)
        #model.Add(grilla[9][1] - grilla[9][2] == 2)
        model.Add(grilla[9][3] == 3)
        model.Add(grilla[9][4] == 6)
        model.Add(grilla[9][5] + grilla[9][6] + grilla[9][7] + grilla[9][8] + grilla[9][9] == 27)
    elif dificultad == 2:
        model.Add(grilla[0][0] + grilla[1][0] + grilla[2][0] == 18)
        model.Add(grilla[0][1] == 10)
        model.Add(grilla[0][2] == 9)
        model.Add(grilla[1][1] == 9)
        model.Add(grilla[0][5] == 2)
        model.Add(grilla[0][4] == 3)
        model.Add(grilla[0][3] + grilla[1][3] + grilla[1][2]== 15)
        model.Add(grilla[1][4] + grilla[1][5] + grilla[1][6]== 10)
        auxm1 = model.NewIntVar(1,336,'auxm1')
        model.AddMultiplicationEquality(auxm1, [grilla[0][6],grilla[0][7]])
        model.AddMultiplicationEquality(336, [auxm1,grilla[0][8]])
        auxm2 = model.NewIntVar(1,100,'auxm2')
        model.AddMultiplicationEquality(auxm2, [grilla[1][8],grilla[1][9]])
        model.AddMultiplicationEquality(100, [auxm2,grilla[0][9]])
        auxm3 = model.NewIntVar(1,72,'auxm3')
        model.AddMultiplicationEquality(auxm3, [grilla[2][6],grilla[2][7]])
        model.AddMultiplicationEquality(72, [auxm3,grilla[1][7]])
        model.Add(grilla[2][1] + grilla[2][3] + grilla[2][2]== 21)
        model.Add(grilla[2][4] == 9)
        auxm4 = model.NewIntVar(1,360,'auxm4')
        model.AddMultiplicationEquality(auxm4, [grilla[3][5],grilla[2][5]])
        model.AddMultiplicationEquality(360, [auxm4,grilla[3][6]])
        model.Add(grilla[3][7] == 4)
        model.Add(grilla[2][9] == 1)
        model.Add(grilla[3][9] + grilla[3][8] + grilla[2][8]== 7)
        model.Add(grilla[3][0] + grilla[4][0] + grilla[4][1]== 17)
        model.Add(grilla[3][1] + grilla[3][2] == 13)
        model.Add(grilla[3][3] + grilla[3][4] + grilla[4][4] == 18)
        model.Add(grilla[4][2] == 3)
        model.AddMultiplicationEquality(40, [grilla[4][3],grilla[5][3]])
        model.Add(grilla[5][6] + grilla[4][5] + grilla[4][6]== 17)
        model.Add(grilla[5][8] + grilla[4][7] + grilla[4][8]== 18)
        auxm5 = model.NewIntVar(1,162,'auxm5')
        model.AddMultiplicationEquality(auxm5, [grilla[5][9],grilla[6][9]])
        model.AddMultiplicationEquality(162, [auxm5,grilla[4][9]])
        model.AddMultiplicationEquality(2, [grilla[5][0],grilla[5][1]])
        auxm6 = model.NewIntVar(1,560,'auxm6')
        model.AddMultiplicationEquality(auxm6, [grilla[5][2],grilla[6][2]])
        model.AddMultiplicationEquality(560, [auxm6,grilla[6][1]])
        model.Add(grilla[6][0] == 9)
        model.Add(grilla[5][4] == 4)
        model.Add(grilla[5][5] == 3)
        auxm7 = model.NewIntVar(1,160,'auxm7')
        model.AddMultiplicationEquality(auxm7, [grilla[6][8],grilla[6][7]])
        model.AddMultiplicationEquality(160, [auxm7,grilla[5][7]])
        
        model.Add(grilla[6][5] == 10)
        model.Add(grilla[6][0] == 9)
        model.AddMultiplicationEquality(10, [grilla[7][1],grilla[8][1]])
        model.Add(grilla[7][2] + grilla[8][2] + grilla[9][2] == 7)
        model.Add(grilla[9][0] + grilla[9][1] == 7)
        model.Add(grilla[9][3] == 7) #
        auxm8 = model.NewIntVar(1,108,'auxm8')
        model.AddMultiplicationEquality(auxm8, [grilla[6][3],grilla[7][3]])
        model.AddMultiplicationEquality(108, [auxm8,grilla[8][3]])
        auxm9 = model.NewIntVar(1,40,'auxm9')
        model.AddMultiplicationEquality(auxm9, [grilla[8][4],grilla[7][4]])
        model.AddMultiplicationEquality(40, [auxm9,grilla[6][4]])
        
        auxm10 = model.NewIntVar(-3,3,'auxm10')
        model.Add( grilla[7][5] - grilla[8][5] == auxm10)
        model.AddAbsEquality(3,auxm10)
        auxm11 = model.NewIntVar(-1,1,'auxm11')
        model.Add( grilla[9][5] - grilla[9][4] == auxm11)
        model.AddAbsEquality(1,auxm11)
        model.Add(grilla[8][7] == 2)
        model.Add(grilla[6][6] + grilla[7][6] + grilla[7][7]== 25)
        model.Add(grilla[9][8] == 9)
        model.Add(grilla[7][9] + grilla[8][9] + grilla[9][9]== 25)
        auxm12 = model.NewIntVar(1,30,'auxm12')
        model.AddMultiplicationEquality(auxm12, [grilla[9][7],grilla[9][6]])
        model.AddMultiplicationEquality(30, [auxm12,grilla[8][6]])

        b = [model.NewBoolVar("b" + str(i)) for i in range(2)]
        t1 = model.NewIntVar(0,100,"t1")
        model.AddDivisionEquality(t1, grilla[7][8], grilla[8][8])
        model.Add(t1 == 8).OnlyEnforceIf(b[0])
        model.Add(t1 != 8).OnlyEnforceIf(b[0].Not())
        t2 = model.NewIntVar(0,100,"t2")
        model.AddDivisionEquality(t2, grilla[8][8],grilla[7][8])
        model.Add(t2 == 8).OnlyEnforceIf(b[1])
        model.Add(t2 != 8).OnlyEnforceIf(b[1].Not())
        model.AddDivisionEquality(8, grilla[7][8], grilla[8][8])
    
    if strategy == 1:
        # Search for x values in increasing order.
        model.AddDecisionStrategy(laux ,cp_model.CHOOSE_FIRST, cp_model.SELECT_MIN_VALUE)
    if strategy == 2:
        # Search for x values in decresing order.
        model.AddDecisionStrategy(laux ,cp_model.CHOOSE_FIRST, cp_model.SELECT_MAX_VALUE)
    if strategy == 3:
        model.AddDecisionStrategy(laux ,cp_model.CHOOSE_FIRST, cp_model.SELECT_LOWER_HALF)
    if strategy == 4:
        model.AddDecisionStrategy(laux ,cp_model.CHOOSE_FIRST, cp_model.SELECT_UPPER_HALF)



def solve(dificultad, strategy):
    #Crear CSP
    model = cp_model.CpModel()
    # Variables y dominios
    grilla = []
    laux = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila += [model.NewIntVar(1, n,'grilla_'+str(i)+str(j))]
            laux.append(model.NewIntVar(1, n,'grilla_'+str(i)+str(j)))
        grilla += [fila]

    restrictions(dificultad, model, grilla, laux, strategy)
    # Solucion
    solver = cp_model.CpSolver()
    solver.Solve(model)
    tiempo = solver.WallTime()
    my_sol = []
    my_sol = [[] for _ in range(n)]
    #print(grilla)
    for i in range(n):
        for j in range(n):
            my_sol[i].append(solver.Value(grilla[i][j]))
    return my_sol, tiempo
