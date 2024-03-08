import abc
import random
import random
import datetime
import json

class SensorSimulator(abc.ABC):
    def __init__(self, topic):
        self.topic = topic

    @abc.abstractmethod
    def simulate_data(self):
        pass

    def publish_data(self, client):
        sensor_id, data, sensor_type = self.simulate_data()

        payload = {
            "id": sensor_id,
            "tipo": sensor_type,
            "temperature": data,
            "timestamp": str(datetime.datetime.now()),
        }
        client.publish(self.topic, json.dumps(payload))
        print(f"Publicado no tópico {self.topic}: {payload}")


class RefrigeratorSensorSimulator(SensorSimulator):
    def simulate_data(self):
        sensor_id = random.randint(1, 100)
        temperature =  random.randint(-3, 12)
        return sensor_id, temperature, "Refrigerator"


class FreezerSensorSimulator(SensorSimulator):
    def simulate_data(self):
        sensor_id = random.randint(1, 100)
        temperature =random.randint(-30, -10)
        return sensor_id, temperature, "Freezer"
