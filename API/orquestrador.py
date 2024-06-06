
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
        return render_template('concatenar.html')
    
    if 'novo_arquivo' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    novo_arquivo = request.files['novo_arquivo']
    base_dir = os.path.dirname(__file__)
    pasta_uploads = os.path.join(base_dir, 'Uploads')
    pasta_downloads = os.path.join(base_dir, 'Downloads')
    
    if not os.path.exists(pasta_uploads):
        os.makedirs(pasta_uploads)
    novo_arquivo_path = os.path.join(pasta_uploads, secure_filename(novo_arquivo.filename))
    
    try:
        novo_arquivo.save(novo_arquivo_path)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


    
    arquivos = os.listdir(pasta_downloads)
    arquivo_existente = None

    for file in arquivos:
        if file.startswith('output'):
            arquivo_existente = os.path.join(pasta_downloads, file)
            break
    # Chamando a função para concatenar e atualizar identificadores
    try:
        arquivo_saida = concatenar_arquivos(arquivo_existente, novo_arquivo_path, pasta_downloads)
        os.remove(arquivo_existente)  # Remove o arquivo existente
        os.remove(novo_arquivo_path)  # Remove o arquivo uploadado pelo usuário
        return jsonify({'message': 'Arquivos concatenados com sucesso!', 'arquivo': arquivo_saida}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    






# @app.route('/validar', methods=['GET'])
# def validar():
#     if 'Identificador' not in request.args:
#         return render_template('validador.html')
    
#     identificador = request.args.get('Identificador')
#     if not identificador:
#         return jsonify(error='Identificador não fornecido'), 400
    
#     # Implementar a lógica de validação
#     if identificador == "12345":
#         return jsonify(mensagem='Identificador válido', nome='Nome Exemplo', cpf='123.456.789-00')
#     else:
#         return jsonify(error='Identificador inválido'), 400


@app.route('/validar', methods=['GET'])
def validar():
    if 'Identificador' not in request.args:
        return render_template('validador.html')
    
    identificador = request.args.get('Identificador')
    if not identificador:
        return jsonify({'error': 'Identificador não especificado'}), 400
    
    try:
        # Caminho para a pasta Downloads
        base_dir = os.path.dirname(__file__)
        downloads_dir = os.path.join(base_dir, 'Downloads')
        
        # Encontrar o arquivo output{x}.xlsx mais recente
        files = [f for f in os.listdir(downloads_dir) if f.startswith('output') and f.endswith('.xlsx')]
        if not files:
            return jsonify({'error': 'Arquivo não encontrado'}), 404
        
        latest_file = max(files, key=lambda f: int(f[len('output'):-len('.xlsx')]))
        file_path = os.path.join(downloads_dir, latest_file)
        
        dataframe = pd.read_excel(file_path)
        resultado, cpf, nome = validate_certificate(identificador, dataframe)
        return jsonify({'mensagem': resultado, 'documento': cpf, 'nome': nome})
    
    except Exception as e:
        return jsonify({'error': f'Erro ao validar identificador: {str(e)}'}), 500

#━━━━━━━━━━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━━━━━━━━━━




if __name__ == '__main__':
    app.run(debug=True)
