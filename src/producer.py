from kafka import KafkaProducer
from logging import log

producer = KafkaProducer(bootstrap_servers='kafka:9092')

def on_success(record):    
    print(record.topic)
    print(record.partition)
    print(record.offset)

def on_error(excp):
    log.error(excp)
    raise Exception(excp)

producer.send('Topic1', {'key': 'value'}).add_callback(on_success).add_errback(on_error)
producer.flush()