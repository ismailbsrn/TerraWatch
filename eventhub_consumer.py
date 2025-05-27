from azure.eventhub import EventHubConsumerClient
from pymongo import MongoClient
import json
from decouple import config

MONGO_URI = config("MONGO_URI")
EVENTHUB_CONNECTION_STR = config("EVENTHUB_CONNECTION_STR")
EVENTHUB_NAME = config("EVENTHUB_NAME")

mongo = MongoClient(MONGO_URI)
collection = mongo.terrawatch.terrawatchcol


def on_event(partition_context, event):
    data = json.loads(event.body_as_str())
    collection.insert_one(data)
    print(f"Inserted: {data}")
    partition_context.update_checkpoint(event)


client = EventHubConsumerClient.from_connection_string(
    conn_str=EVENTHUB_CONNECTION_STR,
    consumer_group="$Default",
    eventhub_name=EVENTHUB_NAME,
)

print("Listening to Event Hub...")
with client:
    client.receive(on_event=on_event)
