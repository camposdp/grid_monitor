
# API para Monitoramento de Linhas de Transmissão

Este projeto consiste em uma API construída com Flask que recebe o status das linhas de transmissão via Serial (do ESP32) e exibe os dados em uma página web. A API se comunica com um ESP32, que envia informações sobre o status das linhas (ligadas/desligadas), e isso é exibido em tempo real na interface web.

## Requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados:

- Python 3.x
- Pip (gerenciador de pacotes do Python)
- Biblioteca `Flask` (para criar a API)
- Biblioteca `pyserial` (para comunicação Serial)
- Um dispositivo ESP32 ou simulação dos dados via Serial

### Instalação das Dependências

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   ```

2. Crie um ambiente virtual (opcional, mas recomendado) e ative-o:
   - Para sistemas Linux ou macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Para Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

4. Se não houver um arquivo `requirements.txt`, você pode instalar as dependências manualmente:
   ```bash
   pip install Flask pyserial
   ```

## Configuração da Porta Serial

Certifique-se de que seu dispositivo ESP32 esteja conectado corretamente à sua máquina. No código da API, ajuste a porta Serial conforme a sua plataforma:
- Para **Windows**, a porta pode ser algo como `COM3`, `COM4`, etc.
- Para **Linux/macOS**, a porta pode ser `/dev/ttyUSB0`, `/dev/ttyS0`, etc.

No arquivo `app.py`, localize a linha abaixo e ajuste para a porta correta:
```python
ser = serial.Serial('COM3', 9600)  # Modifique aqui conforme sua porta
```

## Executando a API

Após configurar o ambiente e ajustar a porta Serial, siga os passos abaixo para executar a API:

1. No terminal, execute o servidor Flask:
   ```bash
   python app.py
   ```

2. O servidor irá iniciar em `http://127.0.0.1:5000`. Você pode acessar esse endereço em seu navegador para visualizar o status das linhas de transmissão.

## Interagindo com a API

A API possui os seguintes endpoints:

- `GET /status_linhas`: Retorna o status das linhas (ligada/desligada) atualizado com base nos dados recebidos via Serial.
- `GET /historico/<linha>`: Retorna o histórico de uma linha específica (linha1, linha2, etc.).

### Exibindo o HTML

- Quando o servidor Flask estiver rodando, abra o navegador e acesse:
  ```
  http://127.0.0.1:5000
  ```

- Na interface, você verá o status de cada linha (ligada/desligada) e poderá clicar nos nomes das linhas para visualizar o histórico de alterações.

## Simulando os Dados da Serial

Caso ainda não tenha o ESP32 configurado ou queira simular os dados, você pode substituir a função de leitura da Serial (`receber_dados_serial()`) por uma função que retorna dados simulados:
```python
def receber_dados_serial():
    return {
        "linha1": 1,
        "linha2": 0,
        "linha3": 1,
        "linha4": 0
    }
```

Essa função irá simular que a `linha1` e a `linha3` estão ligadas, enquanto a `linha2` e a `linha4` estão desligadas.

## Fazendo Push para o Repositório

Se você quiser salvar suas alterações no repositório Git, siga os passos abaixo:

1. Adicione os arquivos modificados:
   ```bash
   git add .
   ```

2. Faça o commit:
   ```bash
   git commit -m "Descrição do commit"
   ```

3. Envie suas alterações para o repositório remoto:
   ```bash
   git push origin main
   ```

## Problemas Comuns

- **Erro na conexão Serial**: Verifique se a porta está correta e se o ESP32 está devidamente conectado.
- **Erro de JSON**: Se o ESP32 estiver enviando dados inválidos, certifique-se de que eles estão no formato JSON correto.
- **Problema ao acessar o servidor**: Certifique-se de que o Flask está rodando e que você está acessando o endereço correto no navegador (`http://127.0.0.1:5000`).

## Contribuições

Sinta-se à vontade para contribuir com o projeto enviando pull requests ou abrindo issues.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
