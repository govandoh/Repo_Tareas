class Nodo:
    def __init__(self, number):
        self.valor = number     # Indica el valor del nodo
        self.izq = None         # Apuntador a el hijo izquierdo
        self.der = None         # Apuntador a el hijo derecho

class ABB:
    def  __init__(self):
        self.raiz = None        # Raíz de la árbol binario de búsqueda

    def integridadABB(self, nodo, valor):
        if nodo == None: 
            return True

        if valor < nodo.valor:
            return self.integridadABB(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.izq == None and valor >= nodo.valor:
                return False
            return self.integridadABB(nodo.der, valor)  
        else:
            print("El número ya existe en el árbol!! \n")
            return False

    def mainInsert(self, valor):        # Inserta un número en el árbol
        if self.integridadABB(self.raiz, valor):
            self.raiz = self.insert(valor, self.raiz)
            print("Número agregado al árbol ABB")
        else:
            print("Error: la inserción haría que el árbol deje de ser un árbol ABB")


    def insert(self, valor, nodo):
        if (nodo == None) :                 # Si el árbol está vacio
            return Nodo(valor)              # Crea un nuevo nodo con el dato introducido y devuelve el mismo

        if (valor < nodo.valor):            # Si el valor es menor que el nodo raíz
            nodo.izq = self.insert(valor, nodo.izq) # Hago que el nodo izquierdo haga una llamada recursiva a insert()

        if (valor > nodo.valor):            # Si el valor es mayor que el nodo raíz
            nodo.der = self.insert(valor, nodo.der) # Hago que el nodo derecho haga una llamada recursiva a insert()

        if (valor == nodo.valor): 
            print("El número ya existe en el árbol \n")

        return nodo                         # Devuelve el nodo creado
    
    #CODIGO NERY C. - ELIMINAR nuevo
    def eliminar(self, valor, nodo):
        if nodo == None:
            return nodo

        if valor < nodo.valor:
            nodo.izq = self.eliminar(valor, nodo.izq)

        elif valor > nodo.valor:
            nodo.der = self.eliminar(valor, nodo.der)

        else:
            if nodo.izq == None:
                return nodo.der

            elif nodo.der == None:
                return nodo.izq

            temp = self.minValueNode(nodo.der)
            nodo.valor = temp.valor
            nodo.der = self.eliminar(temp.valor, nodo.der)

        return nodo

    def minValueNode(self, nodo):
        current = nodo
        while current.izq != None:
            current = current.izq

        return current



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
arbol = ABB()

while True: 
    menuABB()
    opcion = input("Ingrese el numero de la opcion que desea ejecutar: ")
    print(" ")
    try:
        opcion = int(opcion)                # Convierto el string a entero
    except ValueError:
        print("Error: entrada no es número")
    
    if opcion == 6:
        break
    if opcion == 1:
        print("Opcion 1 - Agregar \n")
        numero = input("Ingrese el número que desea insertar al arbol: ")
        try:
            numero = int(numero)        # Convierto el string a entero para insertarlo
            arbol.mainInsert(numero)
        except ValueError:
            print("Error: dato incorrecto para el árbol, ingrese unicamente números")
        print(" ")
    elif opcion == 2: 
        print("Opcion 2 - Buscar \n")
        

        print(" ")
    elif opcion == 3:
        print("Opcion 3 - Eliminar \n")
        numero = input("Ingrese el número que desea eliminar del árbol:")
        try:
            numero = int(numero)
            arbol.eliminar(numero, arbol.raiz)
            print("El número", numero, "fue eliminado del árbol.")
        except ValueError:
            print("Error: dato incorrecto para el árbol, ingrese unicamente números")
        print(" ")

    elif opcion == 4:
        print("Opcion 4 - Cargar desde Archivo txt \n")
        
        print(" ")
    elif opcion == 5: 
        print("Opcion 5 - Visualización Árbol  ABB con Graphviz \n")
        
        print(" ")
    else: 
        print("Opción no valida, ingrese un numero del menu \n")