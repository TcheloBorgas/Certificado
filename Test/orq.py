from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from concat2 import concatenar_arquivos_e_atualizar_identificadores  # Certifique-se de ter a função correta importada
from has import gerar_identificador  # Importar a função de hash
from validacao import validate_certificate  # Importar função de validação, se aplicável
from flask_cors import CORS


app = Flask(__name__,template_folder=r'C:\Users\pytho\Documents\GitHub\Certificado\Frontend')
CORS(app)

@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/concatenar', methods=['POST'])
def upload_concatenar():
    if 'novo_arquivo' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    novo_arquivo = request.files['novo_arquivo']
    pasta_uploads = r'Test\uploads'
    if not os.path.exists(pasta_uploads):
        os.makedirs(pasta_uploads)
    novo_arquivo_path = os.path.join(pasta_uploads, secure_filename(novo_arquivo.filename))
    try:
        novo_arquivo.save(novo_arquivo_path)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Supondo que você tem um arquivo existente com o qual você quer concatenar
    arquivo_existente = os.path.join(pasta_uploads, 'usuarios.xlsx')

    # Chamando a função para concatenar e atualizar identificadores
    try:
        arquivo_saida = concatenar_arquivos_e_atualizar_identificadores(arquivo_existente, novo_arquivo_path)
        return jsonify({'message': 'Arquivos concatenados com sucesso!', 'arquivo': arquivo_saida}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/hash', methods=['GET'])
def hash_cpf():
    cpf = request.args.get('cpf')
    if not cpf:
        return jsonify({'error': 'CPF não especificado'}), 400

    try:
        hash_result = gerar_identificador(cpf)
        return jsonify({'cpf': cpf, 'hash': hash_result})
    except Exception as e:
        return jsonify({'error': 'Erro ao gerar hash', 'detalhe': str(e)}), 500

@app.route('/validar', methods=['GET'])
def validar():
    identificador = request.args.get('identificador')
    if not identificador:
        return jsonify({'error': 'Identificador não especificado'}), 400
    
    try:
        dataframe = pd.read_excel('usuarios.xlsx')
        resultado, cpf = validate_certificate(identificador, dataframe)
        return jsonify({'mensagem': resultado, 'cpf': cpf})
    except Exception as e:
        return jsonify({'error': 'Erro ao validar identificador', 'detalhe': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
