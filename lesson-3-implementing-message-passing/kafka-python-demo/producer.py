from kafka import KafkaProducer


TOPIC_NAME = 'orders'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'{"created_at" : "2020-10-10"}')
producer.flush()
