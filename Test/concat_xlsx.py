import pandas as pd

def concatenar_arquivos_excel(arquivo_existente, novo_arquivo, arquivo_saida=None):
    # Lê os arquivos Excel
    df_existente = pd.read_excel(arquivo_existente)
    df_novo = pd.read_excel(novo_arquivo)
    
    # Concatena os DataFrames
    df_concatenado = pd.concat([df_existente, df_novo], ignore_index=True)
    
    # Define o nome do arquivo de saída, se não for especificado, sobrescreve o arquivo existente
    if arquivo_saida is None:
        arquivo_saida = arquivo_existente
    
    # Salva o DataFrame concatenado em um arquivo Excel
    df_concatenado.to_excel(arquivo_saida, index=False)
    return arquivo_saida

# Exemplo de uso
# arquivo_existente = 'usuarios.xlsx'
# novo_arquivo = 'Dados_Ficticios.xlsx'
# arquivo_saida = 'usuarios_atualizado.xlsx'
# resultado = concatenar_arquivos_excel(arquivo_existente, novo_arquivo, arquivo_saida)
# print(f"Arquivo concatenado salvo em: {resultado}")
