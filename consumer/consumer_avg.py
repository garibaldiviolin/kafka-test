from time import sleep
from kafka import KafkaConsumer


consumer = KafkaConsumer(
    bootstrap_servers='localhost:29092',
    auto_offset_reset='earliest',
    consumer_timeout_ms=1000,
    group_id="my_group"
)
consumer.subscribe(['kafka-python-topic'])

while True:
    for message in consumer:
        print(message)
        consumer.commit()
        sleep(0.1)


consumer.close()
