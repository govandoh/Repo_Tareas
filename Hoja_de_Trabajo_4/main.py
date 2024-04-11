# Archivo main para hacer logica del API. 

from flask import Flask, jsonify, request

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

# Ruta principal

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})
            