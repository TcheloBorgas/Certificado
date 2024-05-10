# Usando uma imagem base com Python 3.9
FROM python:3.9

# Definindo o diretório de trabalho no container
WORKDIR /app

# Copiando os arquivos Python e o requirements.txt
COPY . .

# Instalando as bibliotecas a partir do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão (modifique conforme necessário)
CMD ["python", "orquestrador.py"]
