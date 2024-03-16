from graphviz import Digraph
from colorama import Fore

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
            if nodo.izq == None:
                return True   
            return self.integridadABB(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der == None: 
                return True
            return self.integridadABB(nodo.der, valor)  
        else:
            print(Fore.RED + "El número" , valor,  "ya existe en el árbol!!"+ Fore.RESET)
            return False

    def mainInsert(self, valor):        # Inserta un número en el árbol
        if self.integridadABB(self.raiz, valor):
            self.raiz = self.insert(valor, self.raiz)
            print(Fore.GREEN + "Número: ", valor ,  "agregado al árbol ABB" + Fore.RESET)
        else:
            print(Fore.RED + "Error: la inserción de: ", valor ,  "haría que el árbol deje de ser un árbol ABB \n" + Fore.RESET)


    def insert(self, valor, nodo):
        if (nodo == None) :                 # Si el árbol está vacio
            return Nodo(valor)              # Crea un nuevo nodo con el dato introducido y devuelve el mismo

        if (valor < nodo.valor):            # Si el valor es menor que el nodo raíz
            nodo.izq = self.insert(valor, nodo.izq) # Hago que el nodo izquierdo haga una llamada recursiva a insert()

        if (valor > nodo.valor):            # Si el valor es mayor que el nodo raíz
            nodo.der = self.insert(valor, nodo.der) # Hago que el nodo derecho haga una llamada recursiva a insert()

        return nodo                         # Devuelve el nodo creado
                                           
    def buscar(self, valor, nodo):             #BUSCAR Jaqueline
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self.buscar(valor, nodo.izq)
        else:
            return self.buscar(valor, nodo.der)
    def cargarArchivo(self, path):
        with open(path, 'r') as archivo:                    #Abro el archivo
            for linea in archivo:                           #Recorrido del archivo
                numeros= linea.split(',')                   #Creo una lista de numeros, por cada linea del archivo (cada num esta separado una coma en el archivo, por eso se usa split(',') )
                for num in numeros:
                    try:
                        valor = int(num.strip())            #Intento parsear a tipo entero, cada numero en la lista numeros
                        self.mainInsert(valor)              #Inserto los valores del archivo al ABB (implicitamente uso logica de integridadABB y insert)
                    except ValueError:
                        print(Fore. RED + f"Error: '{num.strip()}' no es un número válido y no se insertará en el árbol. \n" + Fore.RESET)
            print("\n Datos cargados al árbol ABB desde archivo")
        archivo.close                                       #Cierro el archivo
    
    def inorder (self,nodo):
        if nodo is not None:
            if nodo.izq != None:
                self.inorder(nodo.izq)
            print(nodo.valor)
            if(nodo.der != None):
                self.inorder(nodo.der)
    
    #CODIGO NERY C. - ELIMINAR nueva validacion
    def eliminar(self, valor, nodo):
        if nodo == None:
            print(Fore.RED + f"El número: {valor} no existe en el ABB, no se eliminó nada \n" + Fore.RESET)
            return nodo

        if valor < nodo.valor:
            nodo.izq = self.eliminar(valor, nodo.izq)

        elif valor > nodo.valor:
            nodo.der = self.eliminar(valor, nodo.der)

        else:
            print(Fore.GREEN + "El número", numero, "fue eliminado del árbol." + Fore.RESET)
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

    def generar_dot(self, nodo, dot):
        if nodo is not None:
            dot.node(str(nodo.valor))
        if nodo.izq is not None:
            dot.edge(str(nodo.valor), str(nodo.izq.valor))
            self.generar_dot(nodo.izq, dot)
        if nodo.der is not None:
            dot.edge(str(nodo.valor), str(nodo.der.valor))
            self.generar_dot(nodo.der, dot)

    def mostrar_grafico(self):
        dot = Digraph()
        self.generar_dot(self.raiz, dot)
        dot.render('arbol', format='png', view=True, directory='Programacion-III/Repo_Tareas/Tarea 3/ABB_history', cleanup=True)  
        # Guarda el archivo DOT como PNG y lo muestra

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
        numero = input("Ingrese el número que desea buscar en el árbol: ")
        try:
            numero = int(numero)
            encontrado = arbol.buscar(numero, arbol.raiz)
            if encontrado:
                print(f"El número {numero} se encuentra en el árbol.")
            else:
                print(f"El número {numero} no se encuentra en el árbol.")
        except ValueError:
            print("Error: entrada no válida para búsqueda, ingrese unicamente números")
        print(" ")
        

        print(" ")
    elif opcion == 3:
        print("Opcion 3 - Eliminar \n")
        numero = input("Ingrese el número que desea eliminar del árbol:")
        try:
            numero = int(numero)
            eliminado = arbol.eliminar(numero, arbol.raiz)
        except ValueError:
            print("Error: dato incorrecto para el árbol, ingrese unicamente números")
        print(" ")
    elif opcion == 4:
        print("Opcion 4 - Cargar desde Archivo txt \n")
        nombreArchivo = input("Arraste el archivo al terminar para cargar  los numeros: \n")
        try:
            arbol.cargarArchivo(nombreArchivo)
        except FileNotFoundError:
            print("\n Error: No se encontró el archivo indicado")
        print(" ")
    elif opcion == 5: 
        print("Opcion 5 - Visualización Árbol  ABB con Graphviz \n")
        arbol.mostrar_grafico()
        print(" ")
    else: 
        print("Opción no valida, ingrese un numero del menu \n")
