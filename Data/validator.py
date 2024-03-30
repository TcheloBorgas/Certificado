def validate_certificate(identifier, dataframe):
    # Valida o identificador contra o DataFrame.
    if identifier in dataframe['Identificador'].values:
        return "Certificado válido"
    else:
        return "Certificado inválido"
