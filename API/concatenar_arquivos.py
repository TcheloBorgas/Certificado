#━━━━━━━━━━━━━❮Bibliotecas❯━━━━━━━━━━━━━

import pandas as pd

#━━━━━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━━━━━

import pandas as pd
import os  # Importando o módulo os para manipulação de arquivos

# Função auxiliar para ler um arquivo Excel ou usar diretamente um DataFrame
def read_excel_or_dataframe(obj):
    if isinstance(obj, pd.DataFrame):
        return obj
    return pd.read_excel(obj)

# Função principal de concatenação
def concatenar_arquivos(arquivo_existente, novo_arquivo, arquivo_saida=None):
    # Lê os arquivos ou DataFrames diretamente
    df_existente = read_excel_or_dataframe(arquivo_existente)
    df_novo = read_excel_or_dataframe(novo_arquivo)
    
    # Concatena os DataFrames
    df_concatenado = pd.concat([df_existente, df_novo], ignore_index=True)
    
    # Verifica se arquivo_saida é válido e, caso contrário, usa um padrão
    if arquivo_saida is None or not isinstance(arquivo_saida, str):
        arquivo_saida = 'output.xlsx'  # Nome padrão para arquivo de saída

    # Salva o DataFrame concatenado em um arquivo Excel
    df_concatenado.to_excel(arquivo_saida, index=False)
    
    # Exclui o arquivo existente para economizar espaço
    os.remove(arquivo_existente)
    
    return arquivo_saida

