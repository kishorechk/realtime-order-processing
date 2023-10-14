import json

from kafka import KafkaConsumer

from .config import KAFKA_BOOTSTRAP_SERVERS

consumer = KafkaConsumer(
    'order_topic',
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)