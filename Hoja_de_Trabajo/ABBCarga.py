import csv
import time

class nodoArbol:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.valor = valor

class ABB:
    def __init__(self):
        self.raiz = None

    def insert(self, valor):
        self.raiz = self._insert(valor, self.raiz)

    def _insert(self, valor, nodo):
        if nodo is None:
            return nodoArbol(valor)
        
        if(valor < nodo.valor):
            nodo.izq = self._insert(valor, nodo.izq)
        elif(valor > nodo.valor):
            nodo.der = self._insert(valor, nodo.der)
        
        return nodo

    def inorder(self, nodo):
        if nodo is not None:
            self.inorder(nodo.izq)
            print(nodo.valor)
            self.inorder(nodo.der)

# Crear instancia del ABB
abb = ABB()

# Pedir al usuario que seleccione el archivo CSV
archivo_csv = input('Seleccione un archivo CSV: ')

# Iniciar contador de tiempo
inicio_tiempo = time.time()

# Cargar el archivo CSV y agregar cada fila al ABB
with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
    lector_csv = csv.DictReader(csvfile)
    for fila in lector_csv:
        valor = fila['id']  # Suponiendo que 'id' es la columna con los valores a insertar
        abb.insert(valor)

# Finalizar contador de tiempo
fin_tiempo = time.time()

# Mostrar el contenido del árbol ABB
print("Contenido del árbol binario de búsqueda:")
abb.inorder(abb.raiz)

# Calcular y mostrar el tiempo de ejecución
tiempo_ejecucion = fin_tiempo - inicio_tiempo
print(f"Tiempo de ejecución de carga del archivo: {tiempo_ejecucion} segundos")
