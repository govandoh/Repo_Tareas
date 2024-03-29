import csv
import time

class nodoArbol:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.padre  = None
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

    def delete(self, valor):
        self.raiz = self._delete(self.raiz, valor)

    def _delete(self, node, valor):
        if node is None:
            return node

        if valor < node.valor:
            node.izq = self._delete(node.izq, valor)
        elif valor > node.valor:
            node.der = self._delete(node.der, valor)
        else:
            if node.izq is None:
                return node.der
            elif node.der is None:
                return node.leizqft

            node.valor = self._find_min(node.der).valor
            node.right = self._delete(node.der, node.valor)

        return node

    def _find_min(self, node):
        while node.izq is not None:
            node = node.izq
        return node
    
    def _find_max(self, node):
        while node.der is not None:
            node = node.der
        return node
    
    def inorder (self,nodo):
        if nodo is not None:
            if nodo.izq != None:
                self.inorder(nodo.izq)
            if(nodo.der != None):
                self.inorder(nodo.der)
            print(nodo.valor)
            
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
        valor = fila['object id']  # Suponiendo que 'id' es la columna con los valores a insertar
        abb.insert(valor)
# Finalizar contador de tiempo
fin_tiempo = time.time()

tiempo_ejecucion = fin_tiempo - inicio_tiempo
print(f"\n Tiempo requerido de carga masiva: {tiempo_ejecucion} segundos \n")


# Mostrar el contenido del árbol ABB
print("Contenido del árbol binario de búsqueda:")
inicio_tiempo = time.time()
abb.inorder(abb.raiz)
fin_tiempo = time.time()
tiempo_ejecucion = fin_tiempo - inicio_tiempo
print(f"\n Tiempo de ejecución, para mostrar post order: {tiempo_ejecucion} segundos \n")


inicio_tiempo = time.time()
abb.delete('')
fin_tiempo = time.time()
tiempo_ejecucion = fin_tiempo - inicio_tiempo
print(f"\n Tiempo de ejecución, para eliminar: {tiempo_ejecucion} segundos \n")

#338
#13
#7909
#70
#34196
