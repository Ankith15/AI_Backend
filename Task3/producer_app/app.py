from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

KAFKA_BROKER = os.getenv("KAFKA_BROKER")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

@app.route('/register_event', methods=['POST'])
def register_event():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON provided'}), 400

    try:
        producer.send(KAFKA_TOPIC, value=data)
        producer.flush()
        return jsonify({'status': 'event sent to Kafka'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_status', methods=['GET'])
def get_status():
    return jsonify({'status': 'Kafka Producer is running'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
