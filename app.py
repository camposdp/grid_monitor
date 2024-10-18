from flask import Flask, render_template, jsonify
import random
import time
from datetime import datetime

app = Flask(__name__)

# Inicializando o status e histórico das 5 linhas
status_linhas = {
    'linha_1': 'desconhecida',
    'linha_2': 'desconhecida',
    'linha_3': 'desconhecida',
    'linha_4': 'desconhecida',
    'linha_5': 'desconhecida'
}

# Inicializando o histórico de cada linha
historico_linhas = {
    'linha_1': [],
    'linha_2': [],
    'linha_3': [],
    'linha_4': [],
    'linha_5': []
}

# Função que simula a leitura de dados da Serial
def simular_dados_serial():
    time.sleep(1)
    
    linha_1_status = random.choice(['ligada', 'desligada'])
    linha_2_status = random.choice(['ligada', 'desligada'])
    linha_3_status = random.choice(['ligada', 'desligada'])
    linha_4_status = random.choice(['ligada', 'desligada'])
    linha_5_status = random.choice(['ligada', 'desligada'])
    
    linha_serial = f"linha_1:{linha_1_status},linha_2:{linha_2_status},linha_3:{linha_3_status},linha_4:{linha_4_status},linha_5:{linha_5_status}"
    return linha_serial

def atualizar_status_linhas():
    linha_serial = simular_dados_serial()
    
    dados = linha_serial.split(',')
    for dado in dados:
        linha, status = dado.split(':')
        if status_linhas[linha] != status:
            # Atualiza o status e registra o histórico
            status_linhas[linha] = status
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            historico_linhas[linha].append(f"{status} às {timestamp}")

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint para fornecer o status das linhas em JSON
@app.route('/status_linhas', methods=['GET'])
def status_linhas_json():
    atualizar_status_linhas()
    return jsonify(status_linhas)

# Endpoint para fornecer o histórico de uma linha específica
@app.route('/historico/<linha>', methods=['GET'])
def historico_linha(linha):
    if linha in historico_linhas:
        return jsonify(historico_linhas[linha])
    else:
        return jsonify({'error': 'Linha não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
