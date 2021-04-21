from kafka import KafkaProducer
import json


def send_events(producer, topic):
    with open("reprocess_events.txt", "r") as f:
        for line in f.read().splitlines():
            if line == "":
                continue
            data = json.loads(line)
            for key, value in data.items():
                for event in list(value.values())[0]:
                    producer.send(topic, bytes(event, "utf-8"))
                    producer.flush()


if __name__ == "__main__":
    import sys
    broker, topic = sys.argv[1:]
    producer = KafkaProducer(bootstrap_servers=broker)
    send_events(producer, topic)