import pandas as pd

def append_new_data_to_existing_file(existing_file_path, new_data_file_path):
    # Lê o arquivo Excel existente
    existing_df = pd.read_excel(existing_file_path)
    
    # Lê o novo arquivo Excel
    new_data_df = pd.read_excel(new_data_file_path)
    
    # Certifica-se de que apenas as colunas desejadas estão presentes
    new_data_df = new_data_df[['cpf', 'nome', 'email', ]]
    
    # Concatena os novos dados abaixo dos dados existentes
    updated_df = pd.concat([existing_df, new_data_df], ignore_index=True)
    
    # Salva o DataFrame atualizado de volta para o arquivo Excel existente
    updated_df.to_excel(existing_file_path, index=False)

# Caminho para os arquivos Excel
existing_file_path = 'usuarios.xlsx'
new_data_file_path = 'Dados_Ficticios.xlsx'

# Chama a função com os caminhos dos arquivos
append_new_data_to_existing_file(existing_file_path, new_data_file_path)
