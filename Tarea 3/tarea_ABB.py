class Nodo:
    def __init__(self, number):
        self.valor = number     # Indica el valor del nodo
        self.izq = None         # Apuntador a el hijo izquierdo
        self.der = None         # Apuntador a el hijo derecho

class ABB:
    def  __init__(self):
        self.raiz = None        # Raíz de la árbol binario de búsqueda


def menuABB():
    print("----------------------------------------------")
    print("TAREA 3 | Árbol Binario de Busqueda \n")
    print("1. Insertar al ABB")
    print("2. Buscar en el ABB")
    print("3. Eliminar en el ABB")
    print("4. Cargar desde Archivo")
    print("5. Mostrar ABB vía Graphviz")
    print("6. Salir")

opcion = 0

while True: 
    menuABB()
    opcion = input("Ingrese el numero de la opcion que desea ejecutar: ")
    print(" ")
    opcion = int(opcion)
    if opcion == 6:
        break
    if opcion == 1:
        print("Opcion 1 - Agregar \n")
        
        print("Número agregado al árbol ABB")
        print(" ")
    elif opcion == 2: 
        print("Opcion 2 - Buscar \n")
        
        
        print(" ")
    elif opcion == 3:
        print("Opcion 3 - Eliminar \n")
        
        print(" ")
    elif opcion == 4:
        print("Opcion 4 - Cargar desde Archivo txt \n")
        
        print(" ")
    elif opcion == 5: 
        print("Opcion 5 - Visualización Árbol  ABB con Graphviz \n")
        
        print(" ")
    else: 
        print("Opción no valida, ingrese un numero del menu \n")