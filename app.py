from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!:)"

@app.route('/status')
def status():
    return jsonify({"status": "ok"})

@app.route('/data')
def data():
    return jsonify({"data": "Sample data"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
