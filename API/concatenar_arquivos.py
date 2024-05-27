#━━━━━━━━━━━━━❮Bibliotecas❯━━━━━━━━━━━━━

import pandas as pd
from Identificador import gerar_identificador

#━━━━━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━━━━━

# Função auxiliar para ler um arquivo Excel ou usar diretamente um DataFrame
def read_excel_or_dataframe(obj):
    if isinstance(obj, pd.DataFrame):
        return obj
    return pd.read_excel(obj)

# Função principal de concatenação e atualização de identificadores
def concatenar_arquivos_e_atualizar_identificadores(arquivo_existente, novo_arquivo, arquivo_saida=None):
    # Lê os arquivos ou DataFrames diretamente
    df_existente = read_excel_or_dataframe(arquivo_existente)
    df_novo = read_excel_or_dataframe(novo_arquivo)
    
    # Concatena os DataFrames
    df_concatenado = pd.concat([df_existente, df_novo], ignore_index=True)
    
    # Verifica se a coluna 'Identificador' existe e cria se necessário
    if 'Identificador' not in df_concatenado.columns:
        df_concatenado['Identificador'] = None
    
    # Atualiza identificadores onde estão faltando
    mask = df_concatenado['Identificador'].isnull() & df_concatenado['cpf'].notnull()
    df_concatenado.loc[mask, 'Identificador'] = df_concatenado.loc[mask, 'cpf'].apply(gerar_identificador)
    
    # Verifica se arquivo_saida é válido e, caso contrário, usa um padrão
    if arquivo_saida is None or not isinstance(arquivo_saida, str):
        arquivo_saida = 'output.xlsx'  # Nome padrão para arquivo de saída

    # Salva o DataFrame concatenado e atualizado em um arquivo Excel
    df_concatenado.to_excel(arquivo_saida, index=False)
    return arquivo_saida
