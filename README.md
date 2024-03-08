# Simulador Prova 1 módulo 9

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

## Comprovação de funcionamento

### Publisher e Subscriber
![image](https://github.com/lyorrei-inteli/prova1_mod9/assets/99191948/07db5544-58a3-4a5b-a5ef-189d8f06f9f7)


### Testes
![image](https://github.com/lyorrei-inteli/prova1_mod9/assets/99191948/9b49b84a-49e8-4e9d-84a3-01552ffa4520)


## Estrutura do Projeto

- `publisher.py`: Contém o código do publicador que envia dados simulados dos sensores para um Broker MQTT.
- `subscriber.py`: Contém o código do assinante que escuta e printa as mensagens.
- `sensor_simulator.py`: Simula dados dos sensores.
- `tests/`: Pasta contendo os testes automatizados para o simulador.
  - `test_sensor_simulator.py`: Testes automatizados para validar as funcionalidades do simulador.
