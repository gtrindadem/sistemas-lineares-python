import os
import tkinter as tk
from tkinter import filedialog

# Limpa root do tkinter para não abrir nenhum dialog adicional
root = tk.Tk()
root.withdraw()

def buscar_arquivo() -> str:
    arquivo_path = ''
    try:
        arquivo_path = filedialog.askopenfilename()
        print('ARQUIVO ESCOLHIDO:', os.path.basename(arquivo_path), '\n')
    except:
        raise Exception('Ocorreu um erro ao escolher o arquivo! Tente novamente...')

    if arquivo_path == '':
        raise Exception('Você deve escolher um arquivo! Tente novamente...')

    return arquivo_path
