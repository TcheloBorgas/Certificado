from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import os
import sys
sys.path.insert(0, 'c:\\Users\\pytho\\Documents\\GitHub\\Certificado')


# Importando as funções dos módulos Data
from Data.excel_handler import read_excel, write_excel
from Data.identifier import add_identifiers_to_data
from Data.validator import validate_certificate
from Data.excel_handler import read_excel, write_excel
from Data.identifier import add_identifiers_to_data

EXCEL_FILE_PATH = r'C:\Users\pytho\Documents\GitHub\Certificado\usuarios.xlsx'
dataframe = read_excel(EXCEL_FILE_PATH)
dataframe = add_identifiers_to_data(dataframe)
# Salvar as alterações de volta para o arquivo Excel
write_excel(dataframe, EXCEL_FILE_PATH)


app = Flask(__name__,template_folder=r'C:\Users\pytho\Documents\GitHub\Certificado\Frontend')
CORS(app)


# O caminho do arquivo Excel, deve ser alterado para o seu caso específico
EXCEL_FILE_PATH = os.path.join('usuarios.xlsx')

# Carrega os dados do Excel na inicialização do servidor
dataframe = read_excel(EXCEL_FILE_PATH)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/buscar_cpf', methods=['GET'])
def buscar_cpf():
    cpf = request.args.get('cpf')
    if not cpf:
        return jsonify({"erro": "CPF não fornecido"}), 400
    
    global dataframe
    if 'identificador' not in dataframe.columns:
        return jsonify({"erro": "Identificador não gerado para os registros"}), 500

    usuario = dataframe[dataframe['cpf'] == cpf]

    if not usuario.empty:
        identificador = usuario['identificador'].values[0]
        return jsonify({"identificador": identificador})
    else:
        return jsonify({"mensagem": "CPF não encontrado"}), 404



@app.route('/validar_identificador', methods=['GET'])
def validar_identificador():
    identificador = request.args.get('identificador')
    if not identificador:
        return jsonify({"erro": "Identificador não fornecido"}), 400
    
    mensagem = validate_certificate(identificador, dataframe)
    return jsonify({"mensagem": mensagem})

@app.route('/gerar_identificadores', methods=['POST'])
def gerar_identificadores():
    global dataframe
    add_identifiers_to_data(dataframe)
    
    # Após adicionar os identificadores, grava no Excel
    write_excel(dataframe, EXCEL_FILE_PATH)
    
    return jsonify({"mensagem": "Identificadores gerados e salvos com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)
