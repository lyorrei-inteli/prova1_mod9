import time

import paho.mqtt.client as paho
from dotenv import load_dotenv
from paho import mqtt

from sensor_simulator import RefrigeratorSensorSimulator, FreezerSensorSimulator

load_dotenv()

broker_address = 'localhost'
port = 1891

# Inicialização do cliente MQTT
client = paho.Client(paho.CallbackAPIVersion.VERSION2, "python_publisher", protocol=paho.MQTTv5)

client.connect(broker_address, port)

refrigerator_sensor = RefrigeratorSensorSimulator('refrigerator_sensor')
freezer_sensor = FreezerSensorSimulator('freezer_sensor')

if __name__ == "__main__":
    try:
        while True:
            refrigerator_sensor.publish_data(client)
            freezer_sensor.publish_data(client)
            time.sleep(2)  # Esperar 2 segundos antes da próxima publicação
    except KeyboardInterrupt:
        print("Publicação encerrada")
        client.disconnect()
