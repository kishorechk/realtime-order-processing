from kafka import KafkaProducer
import json

from .config import KAFKA_BOOTSTRAP_SERVERS

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
def send_order_event(order_data):
    producer.send('order_topic', value=order_data)