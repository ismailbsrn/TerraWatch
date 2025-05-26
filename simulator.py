import random
import time
import paho.mqtt.client as mqtt
import json

client = mqtt.Client()
client.connect("localhost", 1883)

while True:
    moisture = round(random.uniform(20, 90), 2)
    timestamp = time.time()
    payload = json.dumps({
        "sensor_id": "sensor-1",
        "moisture": moisture,
        "timestamp": timestamp
    })
    client.publish("soil/moisture", payload)
    print(f"Published: {payload}")
    time.sleep(2)

