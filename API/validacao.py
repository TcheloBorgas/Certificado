def validate_certificate(identifier, dataframe):
    try:
        # Busca no DataFrame pelo registro com o identificador fornecido.
        record = dataframe[dataframe['codigo'] == identifier]

        # Verifica se algum registro foi encontrado.
        if not record.empty:
            # Extrai o CPF e o nome do registro encontrado.
            cpf = record['documento'].values[0]  # Assumindo que a coluna com os CPFs se chama 'documento'.
            nome = record['nome'].values[0]  # Assumindo que a coluna com os nomes se chama 'nome'.
            return "Certificado válido", cpf, nome
        else:
            return "Certificado inválido", None, None
    except Exception as e:
        return f"Erro durante a validação: {str(e)}", None, None
