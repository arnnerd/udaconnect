import os

from kafka import KafkaConsumer
from helper import save_set_location

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

# Create the kafka consumer
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_SERVER])

while True:
    for message in consumer:
        location_data = message.value.decode('utf-8')
        
        save_set_location(location_data)