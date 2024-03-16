# Documentación

## Instrucciones de pruebas y ejecución

### Caso de uso: Menú 
El menu incluye 6 opciones: 

1. Insertar al ABB
2. Buscar en el ABB
3. Eliminar en el ABB
4. Cargar desde Archivo
5. Mostrar ABB vía Graphviz
6. Salir

Para este caso de uso, el usuario unicamente debe de ingresar por teclado la opción que desea ejecutar, y el menú se encargará de ejecutar o mostrar la opción que el usuario haya seleccionado. 

### Caso de uso 1: Insertar nuúmero al árbol binario

**Pasos**

1. Seleccionar opción 1 del menú. 
2. Insertar el número que desea insertar al árbol. 
3. El programa internamente hace todos los procedimientos para validar la inserción. 
4. Si es una inserción correcta, se le notifica al usuario por consola, sinó igual notificá la razón porque el número no es válido para ser insertado en el árbol. 

Este caso de, simplemente el usuario, luego de seleccionar la opción 1; se le solicita que ingrese el número que desea agregar al ABB. 

 - Internamente, la opción insertar utiliza la funciones **IntegridadABB**, para validad si el número ya existe o nó en el arbol y también valida si el número insertado haría que el ABB deje de tener sus propiedades necesarias para ser considerado un ABB. 
 - Utiliza tambíen una función secundaria **insert** que recibe como parámetros, el nodo, y el valor, en este caso, al momento de utilizarlo raiz es igual a esta funcion secundaria, que recibe el valor (el número que el usuario está intentando ingresar) y self.raiz como nodo. 
 - Por último la función principal, **mainInsert** únicamente recibe como parámetro el valor (el número que el usuario desea agregar al árbol.)



**Pasos**
1. Seleccionar opción 2 del menú. 
2. Insertar el número que desea Buscar al árbol. 
3. El programa internamente hace todos los procedimientos para validar la busqueda. 
4. Si es una busqueda correcta, se le notifica al usuario por consola, sinó igual notificá la razón porque el número no es válido para ser buscado en el árbol, puede ser que diga que el número se encuentra en el arbol o no se encuentra en el arbol.
   
### Por Ejemplo
Usuario selecciona opción 2; ingresa el número que desea buscar en el ABB

- Internamente, la opción buscar utiliza la funciones **buscar**, para validar si el nodo no existe retornara falso y si nodo tiene valor y es igual al que el usuario registro retornara true luego valida si el valor es menor o mayor que el numero que se registró se realiza una llamada al lado izquierdo o derecho recursiva a buscar.



### Caso de uso: 3 Eliminar un Número del Árbol binario de Busqueda
**Pasos**
1. Ingresar el árbol binario utilizando la opción 1.
2. Ingresa el número que se desea eliminar del árbol binario
3. En dado caso no exista el número en el árbol no se realizara la eliminación, por lo contrario se realizara correctamente.

### Por Ejemplo
1. Ingresar el siguiente arbol binario: 5, 3, 7, 2, 4
2. El arbol quedaria de la siguiente manera:
        5
      /   \
     3     7
    / \    
   2   4

3. Ahora si eliminamos el número 7 del árbol binario de búsqueda, el diagrama quedaría así:
        5
      /   \
     3     5
    /
   2
En este caso, el nodo con el valor 7 tenía un nodo hijo a la izquierda (el nodo con el valor 4), por lo que reemplazamos el valor del nodo con el valor más pequeño del subárbol derecho (el nodo con el valor 5)

Este diagrama se baso en las siguientes condiciones para realizar su eliminación:
-Si el nodo a eliminar no tiene hijos, simplemente eliminarlo.
-Si el nodo a eliminar tiene un hijo, reemplazar el nodo a eliminar con su hijo.
-Si el nodo a eliminar tiene dos hijos, buscar el nodo inmediatamente mayor al nodo a eliminar (sucesor) y reemplazar el nodo a eliminar con este nodo inmediatamente mayor. Luego, eliminar el nodo inmediatamente mayor del árbol.


### Caso de uso 4: Cargar desde archivo .txt
**Pasos**

1. Seleccionar la opción 4 del menú. 
2. Arrastrar el archivo txt el cual desea utilizar para insertar registros al árbol. 
3. **IMPORTANTE**: "Si el ABB no existe, el árbol será creado con los números que existan  en el archivo". 
4. "En el caso que ya exista un árbol creado, al momento de arrastrar el archivo, esto implica que no se genera un nuevo árbol, en cambio solo se cargarán los registros al árbol ya existente". 

**Nota**

Dentro de esta funcionalidad, se reutilizó funciones como integridadABB, insert y mainInsert, debio a que se deben de cumplir las mismas condiciones. 

### Por ejemplo

1. Inserto un árbol a través de la **opción 4**. 
2. Luego intento ingresar un número repetido o ya existente por medio de la **opción 1**.
   1. *"El sistema me indicará que ese dato ya se encuentra registrado".*
3. Luego selecciono de nuevo la **opción 4**, y arrastro un nuevo archivo, con otros números, con números repetidos y diferentes nuevos. 
   1. *"El sistema me indicará que los números repetidos no se pudieron insertar"*
   2. *"Para los números que si eran válidos, me permitirá agregarlos al árbol y notificará cuales fueron agregados".*
   3. *"Para los números que no sean repetidos, pero aun así al insertarlos hacen que el árbol pierda sus dos propiedades principales, me notificará y no permitirá agregarlos al árbol".*

 ***Con todas estas validaciones, comprobamos los diferentes comportamientos posibles que el usuario podría tener en el programa, y así no perder la integridad y propiedades de un árbol binario de búsqueda.***

### Caso de uso 5: Mostrar ABB vía Graphviz
**Pasos**

1. Seleccionar la opción 5 del menú.
2. Abrir el gestor de imagenes para poder visualizar el arbol generado por Graphviz

Internamente para mostrar el ABB utilizamos dos metodos: El primer metodo es una funcion recursiva que toma como argumentos un nodo del arbol y un objeto de Graphviz llamado dot. 
Primero se valida si hay un nodo existente, si lo hay, el volor del nodo se convierte a texto y se añade a un objeto de tipo dot (nuestro grafico). 
Luego se verifica si el nodo actual tiene un hijo izquierdo, si lo tiene, se añade una arista al grafico y se llama recursivamente al mismo metodo en el hijo izquierdo, asi se explora el subarbol izquierdo. 
Luego se verifica si el nodo actual tiene un hijo derecho, si lo tiene, se añade una arista al grafico y se llama recursivamente al mismo metodo en el hijo derecho y asi se explora el subarbol derecho.

El segundo metodo se llama al primer metodo en la raiz del arbol para generar el grafico y luego compila el grafico como un archvo PNG en el directorio especificado en el codigo.


## Ejecución y pruebas

**Prueba y Ejecución Opción 1**
![Opción Insertar en ABB](https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%203/source/opcion_insertarABB.gif)

**Prueba y Ejecución Opción 2**
![Opción Buscar en ABB](https://github.com/govandoh/Repo_Tareas/blob/main/Tarea%203/source/tarea_ABB.py%20-%20Repo_Tareas%20-%20Visual%20Studio%20Code%202024-03-15%2020-19-15.gif)


**Prueba y Ejecución Opción 3**
![Opcion Eliminar de arbol binario](https://github.com/govandoh/Repo_Tareas/blob/main/Tarea%203/source/Prueba%20Eliminar%206.png)


**Prueba y Ejecución Opción 4**
![Opción cargar desde Archivo](https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%203/source/opcion_cargardesdeArchivo.gif)

**Prueba y Ejecución Opción 5**
![Opcion Mostrar ABB via Graphviz](https://github.com/govandoh/Repo_Tareas/blob/main/Tarea%203/source/Prueba_opcion5.gif)

*** 


## Capturas


**Prueba de opciones 1 y 4 (Insertar y cargar desde archivo)**
![Pruebas 1](https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%203/source/pruebas1.png)

![Prueba 2](https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%203/source/pruebas2.png)

![Prueba 3](https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%203/source/pruebas3.png)

![Prueba 4](https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%203/source/pruebas4.png)

**Prueba de opcion 2 (Buscar un nodo del arbol ABB)
![Prueba 1](https://github.com/govandoh/Repo_Tareas/tree/e390de65afb5c76a88286e86a6dc7cc6f25ac382/Tarea%203/source/Buscar_Prueba1)

![Prueba 2](https://github.com/govandoh/Repo_Tareas/tree/e390de65afb5c76a88286e86a6dc7cc6f25ac382/Tarea%203/source/Buscar_Prueba2)

![Prueba 3](https://github.com/govandoh/Repo_Tareas/tree/e390de65afb5c76a88286e86a6dc7cc6f25ac382/Tarea%203/source/Buscar_Prueba3)

![Prueba 4](https://github.com/govandoh/Repo_Tareas/tree/e390de65afb5c76a88286e86a6dc7cc6f25ac382/Tarea%203/source/Buscar_Prueba4)

**Prueba de opcion 3 (eliminar un nodo del arbol ABB)
![Prueba 1](https://github.com/govandoh/Repo_Tareas/blob/main/Tarea%203/source/Prueba%20Eliminar%201.png)

![Prueba 2](https://github.com/govandoh/Repo_Tareas/blob/main/Tarea%203/source/Prueba%20Eliminar%202.png)

![Prueba 3](https://github.com/govandoh/Repo_Tareas/blob/main/Tarea%203/source/Prueba%20Eliminar%203.png)

![Prueba 4](https://github.com/govandoh/Repo_Tareas/blob/main/Tarea%203/source/Prueba%20Eliminar%204.png)

![Prueba 5](https://github.com/govandoh/Repo_Tareas/blob/main/Tarea%203/source/Prueba%20Eliminar%205.png)

![Prueba 6](https://github.com/govandoh/Repo_Tareas/blob/main/Tarea%203/source/Prueba%20Eliminar%206.png)



