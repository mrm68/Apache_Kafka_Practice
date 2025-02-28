from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  # Use the Docker network hostname
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'test-topic'
for i in range(1, 6):
    message = {"number": i, "text": f"Hello Kafka {i}"}
    producer.send(topic=topic, value=message)
    print(f"Sent: {message}")
producer.flush()
