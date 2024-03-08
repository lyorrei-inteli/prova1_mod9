import paho.mqtt.client as paho
from dotenv import load_dotenv
import json

load_dotenv()

broker_address = "localhost"
port = 1891

def freezer_sensor_handler(message):
    if message["temperature"] < -25:
        printMessage = f"{message['tipo']} {message['id']} | {message['temperature']}°C [ALERTA: Temperatura BAIXA]"
    elif message["temperature"] > -15:
        printMessage = f"{message['tipo']} {message['id']} | {message['temperature']}°C [ALERTA: Temperatura ALTA]"
    else:
        printMessage = f"{message['tipo']} {message['id']} | {message['temperature']}°C"
    print(printMessage)
    return printMessage


def refrigerator_sensor_handler(message):
    if message["temperature"] < 2:
        printMessage = f"{message['tipo']} {message['id']} | {message['temperature']}°C [ALERTA: Temperatura BAIXA]"
    elif message["temperature"] > 10:
        printMessage = f"{message['tipo']} {message['id']} | {message['temperature']}°C [ALERTA: Temperatura ALTA]"
    else:
        printMessage = f"{message['tipo']} {message['id']} | {message['temperature']}°C"
    print(printMessage)
    return printMessage


def on_message(client, userdata, message):
    decoded_message = message.payload.decode()
    match message.topic:
        case "freezer_sensor":
            return freezer_sensor_handler(json.loads(decoded_message))
        case "refrigerator_sensor":
            return refrigerator_sensor_handler(json.loads(decoded_message))


def on_connect(client, userdata, flags, rc, _):
    print("Conectado com o código de retorno: ", rc)
    client.subscribe("freezer_sensor")
    client.subscribe("refrigerator_sensor")

if __name__ == "__main__":
    client = paho.Client(
        paho.CallbackAPIVersion.VERSION2, "python_subscriber", protocol=paho.MQTTv5
    )
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker_address, port)

    client.loop_forever()
