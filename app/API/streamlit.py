# IGNORAR POR ENQUANTO


# import streamlit as st
# import pandas as pd
# from concatenar_arquivos import concatenar_arquivos_e_atualizar_identificadores
# from validacao import validate_certificate

# import streamlit as st
# import pandas as pd
# from concatenar_arquivos import concatenar_arquivos_e_atualizar_identificadores

# st.title("API Orquestradora")

# # Upload de arquivo
# uploaded_file = st.file_uploader("Carregue o arquivo novo", type=["xlsx"])
# if uploaded_file is not None:
#     df_novo = pd.read_excel(uploaded_file)
#     # Suponha que você tenha um DataFrame existente carregado de alguma forma
#     df_existente = pd.read_excel(r'C:\Users\pytho\Documents\GitHub\Certificado\API\Uploads\usuarios.xlsx')

#     if st.button("Concatenar e Atualizar Identificadores"):
#         df_resultado = concatenar_arquivos_e_atualizar_identificadores(df_existente, df_novo)
#         st.write(df_resultado)
# else:
#     st.error("Por favor, faça o upload de um arquivo.")


# # Seção de Validação de Identificador
# st.header("Validar Identificador")
# identificador_input = st.text_input("Digite o Identificador")
# if st.button("Validar"):
#     if uploaded_file and identificador_input:
#         df_existente = pd.read_excel(uploaded_file)

#         # Validar o Certificado usando o identificador
#         resultado = validate_certificate(identificador_input, df_existente)

#         # Exibir o resultado da validação
#         if resultado:
#             nome, cpf = resultado  # desempacotando a tupla
#             st.success(f"Identificador válido: Nome - {nome}, CPF - {cpf}")
#         else:
#             st.error("Identificador não encontrado ou inválido.")
#     else:
#         st.error("Por favor, faça upload do arquivo e insira o identificador.")




