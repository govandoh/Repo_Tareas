def menuRecursividad():
    print("----------------------------------------------")
    print("TAREA 2 | FUNCIONES RECURSIVAS \n")
    print("1. Convertir a Binario")
    print("2. Contar Dígitos")
    print("3. Raíz cuadrada Entera")
    print("4. Convertir a decimal desde romano")
    print("5. Suma de numeros enteros")
    print("6. Salir")


#Opcion 1
def convertir_binario(num):
    if(num == 0):
        return " "
    else:
        return convertir_binario(num//2) + str(num%2)

#Opcion 2
def contar_digitos(num):
    if num < 0:
        num = num * -1
        
    if num == 0:
        return 0
    else: 
        return 1 + contar_digitos(num//10)
    
#opcion 3
def calcular_raiz_cuadrada(numero, bajo, alto):
    if bajo <= alto:
        medio = (bajo + alto) // 2
        cuadrado_medio = medio * medio
        
        if cuadrado_medio == numero:
            return medio
        elif numero < cuadrado_medio:
            return calcular_raiz_cuadrada(numero, bajo, medio - 1)
        else:
            return calcular_raiz_cuadrada(numero, medio + 1, alto)
    else:
        return alto

def raiz_cuadrada_entera(numero):
    return calcular_raiz_cuadrada(numero, 0, numero)


#Opcion 5
def sumar_numeros(num): 
    if num == 0:
        return 0
    else:
        return sumar_numeros(num-1)+num

opcion = 0

while True:
    menuRecursividad()
    opcion = input("Ingrese el numero de la función recursiva que desea realizar: ")
    opcion = int(opcion)
    if opcion == 6: 
        break;
    if opcion == 1:
        print("Opcion 1 - Convertir a Binario \n")
        num = int(input("Ingrese el numero que desea convertir a binario: "))
        print("El numero: ", num, "en binario es: ", convertir_binario(num))
    elif opcion == 2: 
        print("Opcion 2 - Contar cantidad de dígitos de un numero entero \n")
        num = int(input("Ingrese el numero que desea contar sus dígitos: "))
        print("El numero ", num, "tiene: ", contar_digitos(num), "digitos")
    elif opcion == 3: 
        print("Opcion 3 - Raiz Cuadrada Entera \n")
        num = int(input("Ingrese el numero al que desee encontrar su raiz cuadrada: "))
        raiz_cuadrada_entera(num)
        print("La raíz cuadrada entera de", num, "es:", raiz_cuadrada_entera(num))
    elif opcion == 4:
        print("Opcion 4 - Convertir a Decimal desde Romanos \n")
    elif opcion == 5:
        print("Opcion 5 - Suma de Numeros enteros \n")
        num = int(input("Ingrese el numero hasta el cual desea contar: "))
        print("La suma de todos los numeros desde 0 hasta:" ,num,  "es: ", sumar_numeros(num))
    else:
        print("Opción no valida, ingrese un numero de las opciones del menu\n")