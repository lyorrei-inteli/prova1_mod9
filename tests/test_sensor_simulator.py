import sys
from pathlib import Path

# Adiciona o diretório pai ao sys.path para que possamos importar sensor_simulator
sys.path.append(str(Path(__file__).parent.parent))

import time

import pytest
from dotenv import load_dotenv

from sensor_simulator import FreezerSensorSimulator, RefrigeratorSensorSimulator
import paho.mqtt.client as paho
import json
from subscriber import freezer_sensor_handler, refrigerator_sensor_handler

load_dotenv()

# Configurações do MQTT
broker_address = "localhost"
port = 1891
refrigerator_topic = "refrigerator_sensor"
freezer_topic = "freezer_sensor"

received_messages = []


# Callback para quando uma mensagem é recebida do broker
def on_message(client, userdata, message):
    received_messages.append((message.topic, json.dumps(message.payload.decode())))


# Setup do cliente MQTT para teste
@pytest.fixture(scope="module")
def mqtt_client():
    client = paho.Client(paho.CallbackAPIVersion.VERSION2, "test_subscriber")
    client.on_message = on_message
    client.connect(broker_address, port)
    client.subscribe(refrigerator_topic)
    client.subscribe(freezer_topic)
    client.loop_start()
    yield client
    client.loop_stop()
    client.disconnect()


def message_reception_check(mqtt_client, sensor, topic):
    sensor_instance = sensor(topic)
    sensor_instance.publish_data(mqtt_client)

    # Espera breve para garantir a recepção da mensagem
    time.sleep(1)

    assert len(received_messages) > 0, "Nenhuma mensagem foi recebida."
    assert (
        received_messages[-1][0] == topic
    ), f"Mensagem recebida no tópico incorreto: {received_messages[-1][0]}"

    # Validação básica dos dados, mais verificações podem ser adicionadas conforme a necessidade
    received_data = received_messages[-1][1]
    assert is_valid_json(received_data), "O formato dos dados recebidos está incorreto."

    received_messages.clear()


# Testa se a mensagem é recebida corretamente
def test_freezer_message_reception(mqtt_client):
    message_reception_check(mqtt_client, FreezerSensorSimulator, freezer_topic)


def test_refrigerator_message_reception(mqtt_client):
    message_reception_check(
        mqtt_client, RefrigeratorSensorSimulator, refrigerator_topic
    )


def sensor_message_alert_check(message_handler, temperature, alert_message):
    printMessage = message_handler(
        {
            "id": 1,
            "tipo": "Freezer",
            "temperature": temperature,
            "timestamp": str(time.time()),
        }
    )
    assert alert_message in printMessage, "Mensagem de alerta incorreta."

    received_messages.clear()


def test_freezer_message_alert():
    sensor_message_alert_check(freezer_sensor_handler, -35, "ALERTA: Temperatura BAIXA")
    sensor_message_alert_check(freezer_sensor_handler, -10, "ALERTA: Temperatura ALTA")


def test_refrigerator_message_alert():
    sensor_message_alert_check(refrigerator_sensor_handler, 1, "ALERTA: Temperatura BAIXA")
    sensor_message_alert_check(refrigerator_sensor_handler, 12, "ALERTA: Temperatura ALTA")


def is_valid_json(myjson):
    try:
        loaded_json = json.loads(myjson)
        if (
            "id" not in loaded_json
            or "tipo" not in loaded_json
            or "temperature" not in loaded_json
            or "timestamp" not in loaded_json
        ):
            return False
    except ValueError as e:
        return False
    return True
