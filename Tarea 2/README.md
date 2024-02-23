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



### Caso de uso: Convertir a decimal desde Romano
**Pasos**



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
