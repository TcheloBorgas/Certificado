
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━❮Bibliotecas❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import os
import pandas as pd

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from concatenar_arquivos import concatenar_arquivos
from validacao import validate_certificate  
from flask_cors import CORS
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━







#━━━━━━━━━━━━━❮Variaveis de controle❯━━━━━━━━━━━━━

app = Flask(__name__,template_folder=r'..\Frontend')
CORS(app)

#━━━━━━━━━━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━━━━━━━━━━




#━━━━━━━━━━━━━❮Rotas❯━━━━━━━━━━━━━


@app.route('/hello')
def hello():
    return "Hello World!"





@app.route('/concatenar', methods=['GET', 'POST'])
def upload_concatenar():
    if request.method == 'GET':
        return render_template(r'concatenar.html')
    if 'novo_arquivo' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    novo_arquivo = request.files['novo_arquivo']
    pasta_uploads = r'..\Uploads'
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
        arquivo_saida = concatenar_arquivos(arquivo_existente, novo_arquivo_path)
        return jsonify({'message': 'Arquivos concatenados com sucesso!', 'arquivo': arquivo_saida}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    








# @app.route('/validar', methods=['GET'])
# def validar():
#     if request.method == 'GET':
#         return render_template(r'validador.html')
    
#     identificador = request.args.get('Identificador')
#     if not identificador:
#         return jsonify({'error': 'Identificador não especificado'}), 400
    
#     try:
#         # Usar um caminho absoluto ou correto para o arquivo Excel
#         base_dir = os.path.dirname(__file__)  # Obter o diretório onde o script está executando
#         file_path = r'..\Uploads\usuarios.xlsx'
        
#         # Garantir que o arquivo existe
#         if not os.path.exists(file_path):
#             return jsonify({'error': 'Arquivo não encontrado'}), 404
        
#         dataframe = pd.read_excel(file_path)
#         resultado, cpf, nome = validate_certificate(identificador, dataframe)
#         return jsonify({'mensagem': resultado, 'cpf': cpf, 'nome': nome})
    
    
#     except Exception as e:
#         return jsonify({'error': f'Erro ao validar identificador {str(e)}', 'detalhe': str(e)}), 500

@app.route('/validar', methods=['GET'])
def validar():
    if request.method == 'GET':
        return render_template(r'validador.html')
    identificador = request.args.get('Identificador')
    if not identificador:
        return jsonify({'error': 'Identificador não especificado'}), 400
    
    try:
        # Caminho absoluto para o arquivo Excel
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, 'uploads', 'usuarios.xlsx')
        
        if not os.path.exists(file_path):
            return jsonify({'error': 'Arquivo não encontrado'}), 404
        
        dataframe = pd.read_excel(file_path)
        resultado, cpf, nome = validate_certificate(identificador, dataframe)
        return jsonify({'mensagem': resultado, 'cpf': cpf, 'nome': nome})
    
    except Exception as e:
        return jsonify({'error': f'Erro ao validar identificador: {str(e)}'}), 500

#━━━━━━━━━━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━━━━━━━━━━




if __name__ == '__main__':
    app.run(debug=True)
