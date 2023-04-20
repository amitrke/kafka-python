from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('Topic1',
                         bootstrap_servers=['kafka:9092'],
           value_deserializer=lambda m: json.loads(m.decode('ascii')))

for message in consumer:
    print(message.topic)
    print(message.partition)
    print(message.offset)
    print(message.key)