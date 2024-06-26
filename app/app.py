import tkinter as tk
from tkinter import filedialog
import pandas as pd
import hashlib

#━━━━━━━━━━━━━❮Funções de Hash❯━━━━━━━━━━━━━

def gerar_identificador(cpf):
    # Cria um hash SHA-256 do CPF
    hash_object = hashlib.sha256(cpf.encode())
    # Retorna os primeiros 10 caracteres do hash hexadecimal
    return hash_object.hexdigest()[:10]

def atualizar_identificadores_no_excel(caminho_arquivo):
    # Lê o arquivo Excel
    df = pd.read_excel(caminho_arquivo)
    
    # Verifica se a coluna 'Identificador' existe, se não existir, cria-a
    if 'Identificador' not in df.columns:
        df['Identificador'] = None

    # Verifica quais linhas estão sem identificador e gera um novo
    df.loc[df['Identificador'].isnull() & df['cpf'].notnull(), 'Identificador'] = df['cpf'].apply(gerar_identificador)
    
    # Salva o DataFrame atualizado em um novo arquivo Excel
    novo_caminho_arquivo = caminho_arquivo.replace('.xlsx', '_atualizado.xlsx')
    df.to_excel(novo_caminho_arquivo, index=False)
    return novo_caminho_arquivo

#━━━━━━━━━━━━━❮Interface Gráfica❯━━━━━━━━━━━━━

def abrir_arquivo():
    root = tk.Tk()
    root.withdraw() # para não mostrar a janela principal do Tk
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if caminho_arquivo:
        novo_arquivo = atualizar_identificadores_no_excel(caminho_arquivo)
        print(f"Arquivo atualizado salvo em: {novo_arquivo}")

abrir_arquivo()
