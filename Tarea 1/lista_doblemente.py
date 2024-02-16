class Alumno: 
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet

class Nodo:
    def __init__(self, alumno):
        self.alumno = alumno
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def agregar_inicio(self,alumno):
        nuevo_nodo = Nodo(alumno)
        nuevo_nodo.siguiente = self.cabeza
        if self.cabeza != None:
            self.cabeza.anterior = nuevo_nodo
        self.cabeza = nuevo_nodo
        
        if self.cola == None:
            self.cola = nuevo_nodo
    
    def agregar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.cola == None:               #Valido si la lista está vaci
            self.cabeza = nuevo_nodo        #hago que el nuevo nodo sea la cola como la cabeza
            self.cola = nuevo_nodo
        else:                                   #entra si la lista no esta hacia, y agregara el nuevo nodo al final
            nuevo_nodo.anterior = self.cola     #el nodo antrior al nuevo sera actualmente la cola de la lista 
            self.cola.siguiente = nuevo_nodo    #se establece que el siguiente nodo de la cola de la lista es el nuevo nodo creado
            self.cola = nuevo_nodo              #se actualiza la referencia de la cola, para que apunte al nuevo nodo creado, nuevo nodo es el ultimo
        
    def imprimir_lista(self):
        actual = self.cabeza
        while actual != None:
            print("Nombre: ", actual.alumno.nombre)
            print("Apellido: ", actual.alumno.apellido)
            print("Carnet: ", actual.alumno.carnet)
            actual = actual.siguiente
        print("None")

    def eliminar(self, valor):
        actual = self.cabeza
        eliminado = False
        if actual == None:                              # Verifico si la lista esta vacia
            eliminado = False
        elif actual.alumno.nombre == valor:             # verifico la el nodo cabeza actual contiene el nombre ingresado (el valor se encuentra en la cabeza)
            self.cabeza = actual.siguiente              # cambio la referencia de la cabeza, la cabeza apuntara al siguiente nodo, del que estoy eliminando
            self.cabeza.anterior = None                 # como cambie la referencia de cabeza, hago que el anterior de cabeza (el nodo que se esta eliminando) apunte a none
            eliminado = True
            print("Nodo Eliminado")
        elif self.cola.alumno.nombre == valor:          # Verifico si en la cola se encuentra el nombre que deseo eliminar
            self.cola = self.cola.anterior              # cambio la referencia de la cola, la cola se mueve hacia el peniultimo y este se convierte en la nueva cola
            self.cola.siguiente = None                  # como ya cambio la cola, digo que el siguiente de la cola es none (asi estoy eliminando el nodo que deseaba eliminar => la cola anterior)
            eliminado = True
            print("Nodo Eliminado")
        else:
            while actual:
                if actual.alumno.nombre == valor:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    eliminado = True
                    print("Nodo Eliminado")
                actual = actual.siguiente
        
        if eliminado == False:
            print("No se encontro un alumno para eliminar")
    

def imprimirMenu():
    print("---------------------------------------")
    print("TAREA 1 - LISTAS DOBLEMENTE ENLAZADAS")
    print("1. Insertar al Inicio")
    print("2. Insertar al final")
    print("3. Eliminar por valor dado")
    print("4. Mostrar Lista")
    print("5. Salir y terminar programa")
    print("---------------------------------------")
    
def solicitarDatos():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    carnet = input("Ingrese carnet: ")
    return nombre, apellido, carnet

opcion = 0
Lista = ListaDoblementeEnlazada()
while True: 
    imprimirMenu()
    opcion = input("Ingrese el numero de la opcion que desea ejecutar: ")
    opcion = int(opcion)
    if opcion == 5:
        break
    if opcion == 1:
        print("Opcion 1")
        datos_Alumno = solicitarDatos()
        nuevoAlumno  = Alumno(*datos_Alumno)
        Lista.agregar_inicio(nuevoAlumno)
        print("Nodo se agrego al inicio")
        print(" ")
    elif opcion == 2: 
        print("Opcion 2")
        datos_Alumno = solicitarDatos()
        nuevoAlumno = Alumno(*datos_Alumno)
        Lista.agregar_al_final(nuevoAlumno)
        print("Nodo se agrego al final")
        print(" ")
    elif opcion == 3:
        print("Opcion 3")
        valor = input("Ingrese el nombre del alumno que desea eliminar")
        Lista.eliminar(valor)
        print(" ")
    elif opcion == 4: 
        print("Se mostrará la lista")
        Lista.imprimir_lista()
    else: 
        print("Opción no valida, ingrese un numero del menu")
    