# Descripcion de la tarea 
Esta tarea tiene como finalidad lograr implementar la utilización de las listas doblmente enlazadas.

Para ello se elaboró un menu para el usuario en el cual puede seleccionar diferentes accciones, que agregaran, eliminarán o mostraráncambios en la lista doblemente enlazada. 

Por último la implementación de Graphviz para generar una representación visual de la lista doblemente enlazada. 
***
# Informacion de estudiante
Nombre: **Gerardo Antonio Ovando Hernandez**
Carnet: **9490-21-7**
Participación: **100%**
***
# Instrucciones de uso del programa

## Caso de uso Menú 
El menu incluye 4 opciones: 

1 - Insertar al inicio. 
2 - Insertar al final
3 - Eliminar por valor 
4 - Mostrar lista 
5 - Salir 
  
Para este caso de uso, el usuario unicamente debe de ingresar por teclado la opción que desea ejecutar, y el menú se encargará de ejecutar o mostrar la opción que el usuario haya seleccionado. 

## Caso de uso: Agregar al inico
En este escenario, se le pide por consola al usuario que ingrese:
 * Nombre
 * Apellido
 * Carnet

Este nuevo elemento (nodo), se agrega al inicio de la lista doblemente enlazada. Pudiendo esta la lista vacia, o si ya tiene elementos, agregarlo hasta el inicio de la lista.   

## Caso de uso: Agregar al Final

Solicitando los mismos parametros, este procesimiento lo que hara es verificar si la lista esta vacia, agrega igualmente al nuevo nodo como la cola y la cabeza. 

Si la lista no esta vacía, entonces con esta opcion el nuevo nodo agregado será el último de la lista. 

## Caso de uso: Eliminar

Por medio de consola, el programa le solicita al usuario que ingrese el nombre del dato (nodo) que desea eliminar. 

La eliminación funciona de la siguiente manera, eliminando el nodo si se encuentra al inicio, al final. 
O si se encuentra en una posición intermedia, elimina el nodo desea y luego reajusta la lista. 

## Caso de uso: Visualizar

Implementando la utilización de Graphviz, al entrar en la opcion 4, se despliega una representación visual de la lista y sus nodos. 

Además, si el usuario hace nuevas inserciones o actualizaciones, al volver a seleccionar la opción 4, se puede ver la represetanción de la lista con los nuevos cambios.
***
## Ejecución y pruebas

Dentro de la carpeta sourse de este proyecto, hay ejemplos de como se ingresan los datos, como se ejecuta y prueba el programa. 

![Insertar ambos casos](https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%201/source/Insertar_Inicio%20Insertar_Final.png)

![Visualizacion Lista Doblemente Enlazada](https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%201/source/Visualizacion_Lista.png)

### Otro ejemplo visual de ejecución
<div>
<p style = 'text-align:center;'>
<iframe width="1000" height = "500"
src="https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%201/source/Ejecucion_DoblementeEnlazada.gif">
</iframe>
</div>
</p>


*** 