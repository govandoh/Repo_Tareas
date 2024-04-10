# Archivo .py para implementar toda la lógica de arbol AVL
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
                return node.izq

            node.valor = self._find_min(node.der).valor
            node.der = self._delete(node.der, node.valor)

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
    
    def cargarArchivo(self):
        archivo_csv = 'Hoja_de_Trabajo_4\source\Air_Quality.csv'
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.DictReader(csvfile)
            for fila in lector_csv:
                #id =  int(fila['Unique ID'])
                #name = str(fila['Name'])
                #place = str(fila['Geo Type Name'])
                #date = str(fila['Start_Date'])
                valor = fila['Unique ID']
                self.insert(valor)
                
abb = ABB()
abb.cargarArchivo()
abb.inorder(abb.raiz)

#abb.delete()