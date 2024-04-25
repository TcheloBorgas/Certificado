def validate_certificate(identifier, dataframe):
    # Busca no DataFrame pelo registro com o identificador fornecido.
    record = dataframe[dataframe['identificador'] == identifier]
    
    # Verifica se algum registro foi encontrado.
    if not record.empty:
        # Extrai o CPF do registro encontrado.
        cpf = record['cpf'].values[0]  # Assumindo que a coluna com os CPFs se chama 'cpf'.
        return "Certificado válido", cpf
    else:
        return "Certificado inválido", None
