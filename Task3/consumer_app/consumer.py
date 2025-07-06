from kafka import KafkaConsumer
import json
import os
from dotenv import load_dotenv
import logging

# ✅ Load .env explicitly from the current folder
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# ✅ Get config from .env
KAFKA_BROKER = os.getenv("KAFKA_BROKER")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

# ✅ Print to confirm values (debug)
print(f"🔌 Connecting to Kafka at: {KAFKA_BROKER}")
print(f"📦 Listening to topic: {KAFKA_TOPIC}")

# ✅ Safety check
if not KAFKA_BROKER or not KAFKA_TOPIC:
    raise Exception("❌ KAFKA_BROKER or KAFKA_TOPIC is not set. Check your .env file and dotenv loading path.")

# ✅ Set up logging to logs/events.log
log_dir = os.path.join(os.path.dirname(__file__), "../logs")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, "events.log"),
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ✅ Initialize Kafka consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='event-consumers',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print(f"✅ Listening to Kafka topic: {KAFKA_TOPIC}...")

# ✅ Consume and log messages
for message in consumer:
    event = message.value
    print(f"📥 Received event: {event}")
    logging.info(json.dumps(event))
