from kafka import KafkaProducer
import json

def send():
    data = {"message":123}
    producer = KafkaProducer(bootstrap_servers='192.168.7.162:9094', value_serializer=lambda v:json.dumps(v).encode("utf-8"))
    kafka_sig = producer.bootstrap_connected()
    print(kafka_sig)
    if kafka_sig:
        producer.send(topic="kafka-task", value={"message":data})
        producer.flush()

if __name__ == "__main__":
    send()