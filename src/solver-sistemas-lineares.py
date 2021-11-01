import os
from utils.leitor_csv import csv_para_list
from ortools.linear_solver import pywraplp

def set_coefficient(constraint, variavel, coefficient):
    constraint.SetCoefficient(variavel, float(coefficient))

def cria_constraint(solver, array_de_variaveis, array_de_coeficientes):
    igualdade = array_de_coeficientes.pop()

    ct = solver.Constraint(float(igualdade), float(igualdade))
    
    for i, var in enumerate(array_de_variaveis):
        set_coefficient(ct, var, array_de_coeficientes[i])

def printar_sistema(solver, variaveis):
    print()

    constraints = solver.constraints()

    for constraint in constraints:
        for i, var in enumerate(variaveis):
            if i > 0:
                print('+', end=' ')

            if constraint.GetCoefficient(var) < 0:
                print(f'({constraint.GetCoefficient(var)})', end=' ')
            else:
                print(f'{constraint.GetCoefficient(var)}', end=' ')
            print(f'* {var}', end=' ')
        print(f'= {constraint.lb()}')
    
    print()


def solve_sistema_linear(input: list):

    solver = pywraplp.Solver.CreateSolver('GLOP')
    variaveis = []

    for i, _ in enumerate(input):
        var = solver.NumVar(-solver.infinity(), solver.infinity(), 'x' + str(i))
        variaveis.append(var)

    for coeficientes_restricao in input:
        cria_constraint(solver, variaveis, coeficientes_restricao)

    printar_sistema(solver, variaveis)

    status = solver.Solve()

    if (status == pywraplp.Solver.OPTIMAL):
        for i, x in enumerate(variaveis):
            print(f'x{i} = {x.solution_value()}')
    else:
        print('Não existe uma solução ótima para este sistema!')


# Main

# O input deve ser no formato:
# a11, a12, ..., a1n, b1
# a21, a22, ..., a2n, b1
# .
# .
# .
# am1, am2, ..., amn, bm
#
# exemplo:
# 2,1,3
# 1,-3,-2

arquivo_csv = os.path.join('inputs_para_teste', 'input2.csv')

arquivo_list = csv_para_list(arquivo_csv)

solve_sistema_linear(arquivo_list)
