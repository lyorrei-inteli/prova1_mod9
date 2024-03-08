# Integração do simulador com Metabase

Este repositório contém um simulador de dispositivos IoT para sensores de refrigeração e um conjunto de testes automatizados para validar o simulador. O simulador publica dados simulados de sensores de temperatura situados em freezers e outros em um refrigeradores. O subscriber printa as mensagens recebidas e valida se deve printar também um alerta de temperatura alta ou baixa.

## Como instalar

Após clonar o repositório, navegue até a pasta do projeto e instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Como rodar o sistema
Para iniciar o simulador, execute o seguinte comando:

```bash
python3 publisher.py
```

Para iniciar o subscriber que irá ouvir as mensagens publicadas pelo simulador, abra um novo terminal e execute:

```bash
python3 subscriber.py
```

## Executar os Testes

Para executar os testes automatizados, use o seguinte comando:

```bash
pytest tests/
```

## Estrutura do Projeto

- `publisher.py`: Contém o código do publicador que envia dados simulados dos sensores para um Broker MQTT.
- `subscriber.py`: Contém o código do assinante que escuta e armazena as mensagens no MongoDB.
- `sensor_simulator.py`: Simula dados dos sensores.
- `tests/`: Pasta contendo os testes automatizados para o simulador.
  - `test_sensor_simulator.py`: Testes automatizados para validar as funcionalidades do simulador.
