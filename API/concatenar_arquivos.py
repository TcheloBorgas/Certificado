#━━━━━━━━━━━━━❮Bibliotecas❯━━━━━━━━━━━━━

import pandas as pd
import os

#━━━━━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━━━━━
# Função auxiliar para ler um arquivo Excel ou usar diretamente um DataFrame
def read_excel_or_dataframe(obj):
    if isinstance(obj, pd.DataFrame):
        return obj
    return pd.read_excel(obj)

# Função principal de concatenação
def concatenar_arquivos(arquivo_existente, novo_arquivo, pasta_saida=None, arquivo_saida_base='output'):
    # Lê os arquivos ou DataFrames diretamente
    df_existente = read_excel_or_dataframe(arquivo_existente)
    df_novo = read_excel_or_dataframe(novo_arquivo)
    
    # Concatena os DataFrames
    df_concatenado = pd.concat([df_existente, df_novo], ignore_index=True)
    
    # Encontrar o próximo número disponível para o arquivo de saída
    i = 1
    while os.path.exists(os.path.join(pasta_saida, f"{arquivo_saida_base}{i}.xlsx")):
        i += 1
    arquivo_saida = f"{arquivo_saida_base}{i}.xlsx"
    caminho_saida = os.path.join(pasta_saida, arquivo_saida)
    
    # Salva o DataFrame concatenado em um arquivo Excel
    df_concatenado.to_excel(caminho_saida, index=False)
    
    return caminho_saida