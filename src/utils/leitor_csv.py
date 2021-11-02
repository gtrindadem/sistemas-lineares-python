import csv

def csv_para_list(arquivo_path: str) -> list:
    linhas = []
    try:
        file = open(arquivo_path)
        reader = csv.reader(file)
        
        for linha in reader:
            linha_number = []
            for item in linha:
                linha_number.append(int(item))
            linhas.append(linha_number)
    except UnicodeDecodeError:
        raise Exception('O arquivo precisa ser um CSV! Tente novamente...')
    except FileNotFoundError:
        raise Exception('Arquivo escolhido não encontrado! Tente novamente...')
    except:
        raise Exception('Ocorreu um erro ao converter o arquivo CSV! Tente novamente...')

    print('LEITURA DO ARQUIVO:', linhas)
    return linhas
