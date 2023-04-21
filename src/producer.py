from kafka import KafkaProducer
from logging import log
import json

producer = KafkaProducer(bootstrap_servers='kafka:9092')

def on_success(record):    
    print(record.topic)
    print(record.partition)
    print(record.offset)

def on_error(excp):
    log.error(excp)
    raise Exception(excp)

topic = 'Topic1'
jsonPayload = {"key": "value"}
encodedPayload = str(jsonPayload).encode('utf-8')
#Send message to kafka
producer.send(topic, encodedPayload).add_callback(on_success).add_errback(on_error)

producer.flush()