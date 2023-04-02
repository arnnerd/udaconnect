import json
import logging
import os

from kafka import KafkaProducer
from typing import Dict

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

# Set logging configuration to INFO level
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-gulp-service")

# Create the kafka producer
producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])

# function used to publish user's location
def publish_set_location(location_data):

    print(f"Data, {location_data}, will be sent to kafka.")

    encoded_data = json.dumps(location_data).encode('utf-8')
    print(f"utf-8 Data, {encoded_data}, will be sent to kafka.")
    producer.send(TOPIC_NAME, encoded_data)
    producer.flush()

    logger.info(f"Published location data {location_data} to kafka successfully.")


