import pandas as pd
import os
import sys


from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from concat_xlsx import concatenar_arquivos_excel  # Correção da importação e nome da função
from has import gerar_identificador  # Correção da importação e nome da função
from validacao import validate_certificate  # Correção da importação e nome da função

app = Flask(__name__,template_folder=r'C:\Users\pytho\Documents\GitHub\Certificado\Frontend')
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/concatenar', methods=['POST'])
def concatenar():
    if 'novo_arquivo' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    novo_arquivo = request.files['novo_arquivo']
    novo_arquivo_path = os.path.join('/caminho/para/uploads', secure_filename(novo_arquivo.filename))
    novo_arquivo.save(novo_arquivo_path)
    
    arquivo_existente = 'usuarios.xlsx'
    resultado = concatenar_arquivos_excel(arquivo_existente, novo_arquivo_path)
    
    return jsonify({'mensagem': 'Arquivos concatenados com sucesso', 'arquivo': resultado})


@app.route('/hash', methods=['GET'])
def hash_cpf():
    cpf = request.args.get('cpf')
    if not cpf:
        return jsonify({'error': 'CPF não especificado'}), 400

    hash_result = gerar_identificador(cpf)
    return jsonify({'cpf': cpf, 'hash': hash_result})

@app.route('/validar', methods=['GET'])
def validar():
    identificador = request.args.get('identificador')
    if not identificador:
        return jsonify({'error': 'Identificador não especificado'}), 400

    # Assumindo que temos um DataFrame carregado previamente (aqui é apenas um exemplo)
    dataframe = pd.read_excel('usuarios.xlsx')  # Exemplo de carga de DataFrame
    resultado, cpf = validate_certificate(identificador, dataframe)
    return jsonify({'mensagem': resultado, 'cpf': cpf})

if __name__ == '__main__':
    app.run(debug=True)
