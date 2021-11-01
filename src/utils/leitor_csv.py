import csv

def csv_para_list(arquivo_path: str) -> list:
    file = open(arquivo_path)

    reader = csv.reader(file)
    linhas = []

    for linha in reader:
        linha_number = []
        for item in linha:
            linha_number.append(int(item))
        linhas.append(linha_number)

    print('LEITURA DO ARQUIVO:', linhas)

    return linhas
