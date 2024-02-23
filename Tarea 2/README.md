# Descripcion de la tarea 


***

# Informacion de estudiante
Nombre: **Gerardo Antonio Ovando Hernandez**
Carnet: **9490-21-7**
Participación: **100%**

Nombre: **Nery Otoniel Colorado Menchú**
Carnet: **9490-22-4867**
Participación: **100%**

Nombre: **Javier David Pirir Gómez**
Carnet: **9490-22-15282**
Participación: **100%**

***

# Documentación

## Instrucciones de pruebas y ejecución

### Caso de uso: Menú 
El menu incluye 6 opciones: 

1. Convertir un número entero a binario. 
2. Contar cantidad de dígitos de un numero entero
3. Raiz Cuadrada Entera
4. Convertir a decimal desde Romano
5. Suma de Números Enteros
6. Salir

Para este caso de uso, el usuario unicamente debe de ingresar por teclado la opción que desea ejecutar, y el menú se encargará de ejecutar o mostrar la opción que el usuario haya seleccionado. 

### Caso de uso: Convertir a binario

**Pasos**
1. En este este caso de uso, se le solicita al usuario que ingrese por consola el numero entero positivo que desea convertir a binario. 

2. Luego de eso la implemenación se encargar de resolver lo solicitado a través de un método en el cual verifica primero si el numero es igual cero, sino a través de la recursividad ejecuta de nuevo el método de binario pero utilizando **div** para que ejecute una división entera  hasta que el cociente sea cero y deteniendose. Y para encontrar la el valor a binario se concatena como string utilizando **mod (%)** del numero dividido dos para encontrar si es resto es 0 o 1.  

**Nota:** el uso de la doble barra "//" se emplea para hacer una división entera más aproximada, sin decimal. 


### Caso de uso: Contar digitos de un numero entero

**Pasos**
1. En este este caso de uso, se le solicita al usuario que ingrese por consola el numero entero al que desea contar la cantidad de dígitos del mismo. 

2. La implementación es una simple función recursiva, en la cual primero se valida si es un numero positivo o negativo, ya que los números enteros abarcan ambos casos. Si es negativo simplemente se multiplica por -1. 
   
3. Luego de eso se comprueba el caso en el cual se detiene la recursividad, que es el punto que siempre nos debemos de preguntar, en este caso es cuando sea 0, porque significa que ya no hay más digitos que contar. 

4. Si no es cero, entonces se retorna la función de nuevo para que haga la división entera **div** del numero//10 y se suma 1. Esto representa que se contó un dígito y que al numero inicial se le redujo 1. 

Por ultimo cuando número ya no tenga dígitos o sea es cero, se retorna el valor general de la función principal que en este caso es la suma de cada ejecución recursiva. 


### Caso de uso: Raiz Cuadrada Entera
**Pasos**

1. En este este caso de uso, se le solicita al usuario que ingrese por consola el numero entero del cual desea encontrar la raiz cuadrada entera.

2. Para la implementación interna, tenemos dos funciones: la primera que nombramos "calcular_raiz_cuadrad" la cual recibe tres argumentos: numero, bajo y alto. Estos argumentos representan el número del cual queremos calcular la raíz cuadrada, y el límite inferior y superior del intervalo de búsqueda. La segunda que nombramos "raiz_cuadrada_entera" la cual recibe el número que queremos sacarle la raíz. Esta función llama a la primera función con el número dado y el rango inicial de 0 a número.

3. Con una condicion, se verifica si el límite inferior es menor o igual que el límite superior. Si no lo es, significa que el intervalo de búsqueda se ha vaciado y no se ha encontrado el valor exacto. En ese caso, se devuelve el límite superior como el valor más cercano.

4. Si el límite inferior es menor o igual que el límite superior, se calcula el punto medio del intervalo con la fórmula (bajo + alto) // 2, donde usamos // para obtener la división entera. Luego, se calcula el cuadrado del punto medio con la fórmula medio * medio.

5. Se compara el cuadrado del punto medio con el número dado. Si son iguales, significa que hemos encontrado la raíz cuadrada exacta y la devolvemos como resultado.

6. Si el cuadrado del punto medio es mayor que el número dado, significa que la raíz cuadrada está en la mitad izquierda del intervalo. Por lo tanto, reducimos el intervalo de búsqueda al subintervalo que va desde el límite inferior hasta el punto medio menos uno. Llamamos de nuevo a la función calcular_raiz_cuadrada con el nuevo intervalo.

7. Si el cuadrado del punto medio es menor que el número dado, significa que la raíz cuadrada está en la mitad derecha del intervalo. Por lo tanto, reducimos el intervalo de búsqueda al subintervalo que va desde el punto medio más uno hasta el límite superior. Llamamos de nuevo a la función calcular_raiz_cuadrada con el nuevo intervalo.


### Caso de uso: Convertir a decimal desde Romano
**Pasos**

1. En este caso de uso, se le solicita al usuario que ingrese el numero romano que se desea convertir a decimal. La cadena de texto ingresada por el usuario se almacenará en la variable "num".

2. Para la implementacion interna, tenemos un metodo y el uso de un diccionario llamado "valores" que almacena nuestros valores pares de clave-valor que usaremos en el metodo. Dado que usaremos letras, daremos valores a esas letras para posteriormente operar esos valores y obtener el numero transformado de romano a decimal. 

3. Nuestro método comienza comparando la longitud de la cadena de caracteres almacenado en la variable "romano", si es igual a 0 entonces devolveremos el valor de cero.

4. Si la longitud de la cadena no es igual a 0, agregando otra comprobacion, comprobamos si la longitud de la cadena de caracteres almacenado en la variable "romano", si tiene solo un carácter o si el primer carácter tiene un valor mayor o igual que el segundo. Si se cumple alguna de estas condiciones, devuelve el valor del primer carácter más el resultado de llamar a la misma función con el resto de la cadena como argumento. Para seguir comparando el resto de el resto de caracteres en la cadena, llamamos a la misma funcion hasta comparar satisfactoriamente todos los caracteres. 

5. Sino, si el primer carácter tiene un valor menor que el segundo, devuelve la diferencia entre el valor del segundo y el primer carácter más el resultado de llamar a la misma función con el resto de la cadena a partir del tercer carácter como argumento. Para seguir comparando el resto de el resto de caracteres en la cadena, llamamos a la misma funcion hasta comparar satisfactoriamente todos los caracteres. 


### Caso de uso: Suma de números enteros 
**Pasos**

1. En este este caso de uso, se le solicita al usuario que ingrese hasta que numero desea que se haga la sumatoria. 

2. La implementación interna, es una función recursiva que primero hace la validación si número es igual a cero, que es nuestro "break" o la condición que nos debemos de preguntar, para que se detenga la función recursiva. 
   
3. Sino es cero, entonces simplemente se hace un retorno, llamando de nuevo la función recurvisa, solo que haciendo una resta de **n-1** y sumarlo a n. 

Ejemplo 
Ingreso = 5
sumar_numeros(n-1) + n 

4. En la ultima ejecución cuando número sea igual a cero, la función retornará la suma que se realizó recursivamente. 


## Ejecución y pruebas


**Prueba y Ejecución Opcion 1**
![Ejecución Opcion 1](https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%202/source/Opcion1_Binario.png)

**Prueba y Ejecución Opcion 2**
![Ejecución Opcion 2](https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%202/source/Opcion2_ContarDigitos.png)

**Prueba y Ejecución Opcion 3**
![Ejecución Opcion 3](https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%202/source/Opcion3_RaizEntera.png)

**Prueba y Ejecución Opcion 4**
![Ejecución Opcion 4](https://raw.githubusercontent.com/govandoh/Repo_Tareas/main/Tarea%202/source/Opcion4_DecimalToRomano.png)

**Prueba y Ejecución Opcion 5**
![Ejecución Opcion 5](https://github.com/govandoh/Repo_Tareas/blob/main/Tarea%202/source/Opcion5_SumaEnteros.png)
*** 
