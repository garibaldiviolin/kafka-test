from time import sleep
from kafka import KafkaProducer
import json
import random

# Create an instance of the Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Call the producer.send method with a producer-record
print("Ctrl+c to Stop")
# while True:
for _ in range(100):
    producer.send(
        'kafka-python-topic', {"number": random.randint(1, 999)}
    )

sleep(10)
