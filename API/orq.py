from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import os
import hashlib
from Identificador import gerar_identificador
from validacao import validate_certificate
from concatenar_arquivos import concatenar_arquivos_e_atualizar_identificadores

app = Flask(__name__)

# Rota para servir a página de concatenar arquivos
@app.route('/concatenar')
def concatenar():
    return send_from_directory('.', 'concatenar.html')

# Rota para servir a página de validar certificados
@app.route('/validador')
def validador():
    return send_from_directory('.', 'validador.html')

# Rota para concatenar arquivos
@app.route('/concatenar', methods=['POST'])
def concatenar_arquivos():
    if 'novo_arquivo' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    novo_arquivo = request.files['novo_arquivo']
    caminho_arquivo_existente = 'arquivo_existente.xlsx'  # Caminho do arquivo existente

    # Chama a função para concatenar e atualizar identificadores
    try:
        arquivo_saida = concatenar_arquivos_e_atualizar_identificadores(caminho_arquivo_existente, novo_arquivo)
        return jsonify({'message': f'Arquivo concatenado com sucesso! Salvo como {arquivo_saida}'})
    except Exception as e:
        return jsonify({'error': f'Erro ao concatenar arquivos: {str(e)}'}), 500

# Rota para validar identificador
@app.route('/validar', methods=['GET'])
def validar_identificador():
    identificador = request.args.get('Identificador')
    if not identificador:
        return jsonify({'error': 'Identificador não especificado'}), 400

    try:
        caminho_arquivo = 'usuarios.xlsx'  # Caminho do arquivo de usuários
        if not os.path.exists(caminho_arquivo):
            return jsonify({'error': 'Arquivo não encontrado'}), 404

        dataframe = pd.read_excel(caminho_arquivo)
        mensagem, cpf, nome = validate_certificate(identificador, dataframe)
        return jsonify({'mensagem': mensagem, 'cpf': cpf, 'nome': nome})
    except Exception as e:
        return jsonify({'error': f'Erro ao validar identificador: {str(e)}'}), 500

# Restrição de acesso ao Marcelo
@app.before_request
def restrict_access():
    if request.path == '/validador' and not user_is_marcelo():
        return "Acesso negado", 403

def user_is_marcelo():
    # Implementar lógica de autenticação
    # Exemplo simplificado:
    return request.headers.get('X-User') == 'Marcelo'

if __name__ == '__main__':
    app.run(debug=True)
