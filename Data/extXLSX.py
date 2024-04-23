import pandas as pd

def append_and_overwrite_excel(existing_file_path, new_data_file_path):
    # Carregar o arquivo Excel existente
    existing_df = pd.read_excel(existing_file_path)
    
    # Carregar o arquivo com novos dados
    new_data_df = pd.read_excel(new_data_file_path)
    
    # Concatenar os DataFrames
    updated_df = pd.concat([existing_df, new_data_df], ignore_index=True)
    
    # Salvar o DataFrame atualizado, sobrescrevendo o arquivo Excel existente
    updated_df.to_excel(existing_file_path, index=False)

# Exemplo de uso
# append_and_overwrite_excel('caminho_para_o_arquivo_existente.xlsx', 'caminho_para_novos_dados.xlsx')


def update_database_with_new_file(new_file_path):
    # Este é apenas um exemplo simplificado
    # Você precisaria ajustar esta função para atender às suas necessidades específicas
    existing_df = pd.read_excel('usuarios.xlsx')
    new_data_df = pd.read_excel(new_file_path)
    updated_df = pd.concat([existing_df, new_data_df], ignore_index=True)
    updated_df.to_excel('usuarios.xlsx', index=False)
    

# interligar com a api
def standardize_data(file_path):
    # Lê o arquivo Excel
    df = pd.read_excel(file_path)
    
    # Padroniza os nomes das colunas: remove espaços, converte para minúsculas
    df.columns = df.columns \
        .str.strip() \
        .str.lower() \
        .str.replace(' ', '_') \
        .str.replace('ç', 'c', regex=False)
    
    # Padroniza o formato do CPF: apenas números, removendo pontos e traços
    df['cpf'] = df['cpf'].astype(str).str.replace('\D', '', regex=True)
    
    # Padroniza o formato do email: convertendo para minúsculas
    df['email'] = df['email'].str.lower()
    
    # Trata outros campos conforme a necessidade aqui
    
    # Retorna o DataFrame limpo
    return df

# Caminho para o arquivo Excel
file_path = 'caminho_para_seu_arquivo.xlsx'

# Chama a função e passa o caminho do arquivo
df_clean = standardize_data(file_path)

# Salva o DataFrame padronizado de volta em um arquivo Excel
df_clean.to_excel('caminho_para_arquivo_padronizado.xlsx', index=False)
