import serial
import json
from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# Configurando a porta Serial (modifique conforme a porta correta e o baudrate do ESP32)
ser = serial.Serial('COM3', 9600)  # Para Windows use COM3, COM4, etc. Para Linux use '/dev/ttyUSB0', etc.

# Inicializando o status das linhas
status_linhas = {
    'linha1': 'desconhecida',
    'linha2': 'desconhecida',
    'linha3': 'desconhecida',
    'linha4': 'desconhecida'
}

def receber_dados_serial():
    """Função para ler dados via Serial do ESP32 e retornar como um dicionário."""
    if ser.in_waiting > 0:  # Verifica se há dados disponíveis na Serial
        dados = ser.readline().decode('utf-8').strip()  # Lê e decodifica a linha
        try:
            # Converte a string JSON recebida via Serial para um dicionário Python
            status = json.loads(dados)
            return status
        except json.JSONDecodeError:
            print("Erro ao decodificar JSON:", dados)
            return None
    return None

def atualizar_status_linhas():
    """Atualiza o status das linhas com base nos dados recebidos via Serial."""
    status = receber_dados_serial()
    if status:
        for linha, estado in status.items():
            if estado == 1:
                status_linhas[linha] = 'ligada'
            elif estado == 0:
                status_linhas[linha] = 'desligada'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status_linhas', methods=['GET'])
def status_linhas_json():
    # Atualiza o status das linhas lendo os dados da Serial
    atualizar_status_linhas()
    return jsonify(status_linhas)

if __name__ == '__main__':
    app.run(debug=True)
