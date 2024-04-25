import pandas as pd
from has import gerar_identificador

def concatenar_arquivos_e_atualizar_identificadores(arquivo_existente, novo_arquivo, arquivo_saida=None):
    # Lê os arquivos Excel
    df_existente = pd.read_excel(arquivo_existente)
    df_novo = pd.read_excel(novo_arquivo)
    
    # Concatena os DataFrames
    df_concatenado = pd.concat([df_existente, df_novo], ignore_index=True)
    
    # Verifica se a coluna 'Identificador' existe e cria se necessário
    if 'Identificador' not in df_concatenado.columns:
        df_concatenado['Identificador'] = None
    
    # Atualiza identificadores onde estão faltando
    mask = df_concatenado['Identificador'].isnull() & df_concatenado['cpf'].notnull()
    df_concatenado.loc[mask, 'Identificador'] = df_concatenado.loc[mask, 'cpf'].apply(gerar_identificador)
    
    # Define o nome do arquivo de saída, se não for especificado, sobrescreve o arquivo existente
    if arquivo_saida is None:
        arquivo_saida = arquivo_existente
    
    # Salva o DataFrame concatenado e atualizado em um arquivo Excel
    df_concatenado.to_excel(arquivo_saida, index=False)
    return arquivo_saida
