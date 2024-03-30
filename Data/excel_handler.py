import pandas as pd

def read_excel(file_path):
    # Lê o arquivo Excel e retorna um DataFrame.
    return pd.read_excel(file_path)

def write_excel(dataframe, file_path):
    # Escreve o DataFrame em um arquivo Excel.
    dataframe.to_excel(file_path, index=False)
