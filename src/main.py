from solver_sistemas_lineares import solve_sistema_linear
from utils.buscar_arquivo import buscar_arquivo
from utils.leitor_csv import csv_para_list

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

def main():
    print('Escolha um arquivo CSV para resolver o sistema linear:')
    try:
        arquivo_path = buscar_arquivo()
        arquivo_list = csv_para_list(arquivo_path)
        solve_sistema_linear(arquivo_list)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
