# Archivo main para hacer logica del API. 

import csv
import os
from flask import Flask, jsonify, request

from AVL_tree import AVLTree

app = Flask(__name__)
avl_tree = AVLTree()

@app.route("/")
def root():
    return jsonify({'message': 'API implementada para hoja de trabajo 4'})

@app.route('/cargarCSV', methods=['POST'])
def createByFile():
    try:
        file_repo = os.path.dirname(os.path.abspath(__file__))
        archivo_csv = os.path.join(file_repo, 'source', 'Air_Quality_desordenado.csv')
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
                lector_csv = csv.DictReader(csvfile)
                for fila in lector_csv:
                    valor = fila['Unique ID']
                    avl_tree.insert(valor)
        return jsonify({'Message': 'Successfull, Arbol AVL generado Correctamente'}), 200
    except Exception as e:
        return jsonify({'Error:' f'Error al generar el arbol AVL {e}'}), 400
    
@app.route('/viewTree', methods=['GET'])
def viewTree():
    nodes = avl_tree.get_all_nodes()
    
    return jsonify({'nodos': nodes}),200
        
    
if __name__ == '__main__':
    app.run(debug=True)
    
            
