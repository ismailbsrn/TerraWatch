from azure.eventhub import EventHubProducerClient, EventData
import paho.mqtt.client as mqtt
from decouple import config

connection_str = config('CONNECTION_STRING')
eventhub_name = config('EVENT_HUB_NAME')

producer = EventHubProducerClient.from_connection_string(conn_str=connection_str, eventhub_name=eventhub_name)

def send_to_eventhub(message):
    try:
        event_data_batch = producer.create_batch()
        event_data_batch.add(EventData(message))
        producer.send_batch(event_data_batch)
    except Exception as e:
        print(f"Failed to send to Event Hub: {e}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"Received MQTT message: {payload}")
    send_to_eventhub(payload)
    print("Sent to Event Hub")

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883)
client.subscribe("soil/moisture")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Exiting...")

producer.close()
