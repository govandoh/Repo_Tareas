import csv
import time  # Importamos el módulo time

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar_elemento(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def retirar_primero(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente

    def retirar_ultimo(self):
        if not self.cabeza or not self.cabeza.siguiente:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente:
                actual = actual.siguiente
            actual.siguiente = None

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Crear una instancia de ListaSimple
mi_lista = ListaSimple()

# Pedir al usuario que seleccione el archivo CSV
archivo_csv = input('Seleccione un archivo CSV: ')

inicio_tiempo = time.time()  # Iniciar el contador de tiempo

# Cargar el archivo CSV y agregar cada fila a la lista simple
with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
    lector_csv = csv.DictReader(csvfile)
    for fila in lector_csv:
        mi_lista.agregar_elemento(fila['CT'])       #Para que los archivos se lean hay que cambiar el identificador de la columna que se desea tomar. 

fin_tiempo = time.time()  # Finalizar el contador de tiempo

tiempo_ejecucion = fin_tiempo - inicio_tiempo
print(f" \n Tiempo de ejecución: {tiempo_ejecucion} segundos, para hacer prueba de carga masiva \n")


# Mostrar los datos de la lista
inicio_tiempo = time.time()

print("Contenido de la lista cargado desde el archivo CSV:")
mi_lista.imprimir_lista()

fin_tiempo = time.time()

# Calcular el tiempo de ejecución
tiempo_ejecucion = fin_tiempo - inicio_tiempo
print(f"\n Tiempo de ejecución: {tiempo_ejecucion} segundos, requerido para mostrar la carga masiva \n")


inicio_tiempo = time.time()

mi_lista.retirar_ultimo()

fin_tiempo = time.time()

tiempo_ejecucion = fin_tiempo - inicio_tiempo
print(f"\n Tiempo de ejecución: {tiempo_ejecucion} segundos, requerido eliminar último \n")