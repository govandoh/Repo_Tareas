# Documentación

## Instrucciones

### Cargar registros desde un archivo CSV

**Pasos**

1. Tomar en cuenta que al ser un metodo post se debe usar una herramienta como postman, (no es necesario params o body)
2. En postman, simplemente seleccionar la opción de método post. 
3. Ingresar el siguiente URL: https://repo-tareas.onrender.com/cargarCSV
4. Luego de eso, el retorno, será satisfactorio, por lo cual, la carga masiva se realizó correctamente. 

**Nota**
Para comprobar que si funcionó la carga masiva, puede utilizar desde cualquier navegador, el siguiente metodo GET, para visualizar el árbol AVL. 
http://127.0.0.1:5000/viewTree


### Insertar manualmente

**Pasos**
1. Tomar en cuenta que al ser un metodo post se debe usar una herramienta como postman, (es necesario el uso del body)
2. En postman, simplemente seleccionar la opción de método post. 
3. Ingrese el siguiente URL: https://repo-tareas.onrender.com/insertarRegistro
4. Seleccionar Body > Raw: 
5. La estructura json es la siguiente

{
    "Unique ID": "el numero a ingresar"
}

**Nota**
Para comprobar que si funcionó la inserción manual, puede utilizar desde cualquier navegador, el siguiente metodo GET, para visualizar el árbol AVL. 
http://127.0.0.1:5000/viewTree

### Buscar registro

***Pasos**
1. Desde el navegador ingrese el siguiente URL: https://repo-tareas.onrender.com/buscarRegistro/
2. Despues de /, ingrese el numero de registro que desea buscar.
3. Presione enter y se mostrará como respuesta json si el número existe o no en el árbol AVL.
