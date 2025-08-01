
from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/balance')
def balance():
    return jsonify({'ltc': 1.23, 'usd': 95.00})

@app.route('/api/start', methods=['POST'])
def start():
    return jsonify({'status': 'Bot started'})

@app.route('/api/stop', methods=['POST'])
def stop():
    return jsonify({'status': 'Bot stopped'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
