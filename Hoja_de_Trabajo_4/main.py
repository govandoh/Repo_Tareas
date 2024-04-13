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

#Punto 1 - Cargar registros desde un archivo CSV
#Tomar en cuenta que al ser un metodo post se debe usar una herramienta como postman, (no es necesario params o body)

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
        

##Punto 2 - Inserción manual de registros
@app.route('/insertarRegistro', methods=['POST'])
def insertarRegistro():
    try:
        # Recibe los datos del registro de la solicitud HTTP
        data = request.get_json()
        
        # Asegúrate de que los datos recibidos contienen la información necesaria para insertar en el árbol
        if 'Unique ID' not in data:
            return jsonify({'error': 'El campo "Unique Id" es requerido'}), 400
        
        # Inserta el registro en el árbol AVL
        avl_tree.insert(data['Unique ID'])
        
        return jsonify({'message': 'Registro insertado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': f'Error al insertar el registro: {e}'}), 500

##Punto 3 - Busqueda de registros
@app.route('/buscarRegistro/<id>', methods=['GET'])
def buscarRegistro(id):
    try:
        nodo = avl_tree.search(id)
        mensaje = 'Succesfull, status:200'
        if nodo is None:
            return jsonify({'error': 'Registro no encontrado'}), 404
        response = {
            'message': mensaje,
            'Unique ID': nodo.key
        }      
        return response, 200
    except Exception as e:
        return jsonify({'error': f'Error al buscar el registro: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
    ##Punto 4 Mostrar información del grupo: 

from flask import Flask, jsonify

app = Flask(_name_)

@app.route('/nombres', methods=['GET'])
def get_data():
    # Datos quemados
    data = {
        "Nombre": "Jaqueline Mariela Figueroa",
        "Carnet": "9490-21-4689"
    }
    data2 ={
        "Nombre": "Gerardo Antonio Ovado",
        "Carnet": "9490-21-7"
    }
    data3 ={
        "Nombre": "Nery Otoniel Colorado",
        "Carnet": "9490-22-4867"
    }
    data4 ={
        "Nombre": "Javier Pirir Gomez",
        "Carnet": "9490-22-15282"
    }
    return jsonify({"data": data, "data2": data2, "data3":data3, "data4":data4 })

if _name_ == '_main_':
    app.run(debug=True)
    
