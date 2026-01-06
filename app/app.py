import os, json, logging
from flask import Flask, jsonify, Response
from prometheus_client import Gauge, generate_latest
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(msg='Simple Python App')

@app.route('/health')
def health():
    return jsonify({'success':True})

@app.route('/version')
def version():
    return jsonify(msg='Version 1.0')

@app.route('/code')
def code():
    if "Code" in os.environ:
        return jsonify({'Code': os.environ['Code']})
    else:
        return jsonify({'Code': 'You forgot to use env ...'})

metric = Gauge('metric_desafio', 'Sample metric do desafio de observability')

def set_metric():
    metric.set(777)

@app.route("/metrics")
def metrics():
    set_metric()
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=8008)
