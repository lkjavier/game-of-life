from kafka import KafkaProducer
import json
producer = KafkaProducer(bootstrap_servers='kafkacluster_kafka:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                         api_version=(0, 10, 1))
for i in range(0, 100):
	producer.send("gameoflife", {"message":"test" + str(i)})
producer.flush()
print("done with producing")