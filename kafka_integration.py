# --- kafka_integration.py ---
# Integrate Kafka for real-time processing
from kafka import KafkaConsumer, KafkaProducer
import json

def consume_messages(topic):
    """Consume messages from Kafka topic."""
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id='fraud-detection-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        print("Received message:", message.value)

def produce_message(topic, message):
    """Produce messages to Kafka topic."""
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    producer.send(topic, value=message)
