import random
import string

def generate_unique_identifier(existing_ids):
    # Gera um identificador único.
    while True:
        identifier = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        if identifier not in existing_ids:
            return identifier

def add_identifiers_to_data(dataframe):
    # Adiciona identificadores únicos ao DataFrame.
    existing_ids = set(dataframe['Identificador'].dropna().unique())
    dataframe['Identificador'] = [
        generate_unique_identifier(existing_ids) if pd.isnull(row['Identificador']) else row['Identificador']
        for index, row in dataframe.iterrows()
    ]
