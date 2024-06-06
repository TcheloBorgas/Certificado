import pandas as pd
import random
import string

# Função para gerar um CPF fictício
def gerar_cpf():
    def calcular_digito(cpf):
        if len(cpf) == 9:
            peso = list(range(10, 1, -1))
        elif len(cpf) == 10:
            peso = list(range(11, 1, -1))
        else:
            raise ValueError("CPF deve ter 9 ou 10 dígitos antes dos dígitos verificadores.")
        
        soma = sum(int(cpf[i]) * peso[i] for i in range(len(cpf)))
        digito = 11 - (soma % 11)
        return str(digito) if digito < 10 else '0'
    
    base_cpf = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    cpf = base_cpf + calcular_digito(base_cpf)
    cpf = cpf + calcular_digito(cpf)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# Função para gerar um identificador único
def gerar_identificador(tamanho=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=tamanho))

# Gerar 10 usuários fictícios
usuarios = []
for i in range(10):
    cpf = gerar_cpf()
    nome = f"Nome{random.randint(1, 100)}"
    email = f"{nome.lower()}@exemplo.com"
    identificador = gerar_identificador()
    usuarios.append([cpf, nome, email, identificador])

# Criar um DataFrame com os dados
colunas = ['documento', 'nome', 'email', 'codigo']
df_usuarios = pd.DataFrame(usuarios, columns=colunas)

# Salvar o DataFrame em uma nova planilha Excel
output_file_path = 'output.xlsx'
df_usuarios.to_excel(output_file_path, index=False)

output_file_path
