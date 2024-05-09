import csv
import os
from graphviz import Digraph

class SparseMatrix:
    def __init__(self):
        self.matrizD = []
        self.matriz_esquema = []
    
    def leer_csv(self, nombre_archivo):
        with open(nombre_archivo, 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            encabezados = next(lector_csv)
            for fila in lector_csv:  # Por cada fila en el archivo CSV
                self.matrizD.append(fila)   # Agregamos la fila como una lista a la matriz
    
    def convert_esquema(self):
        matriz_datos = self.matrizD
        columnas = matriz_datos
        columnas_filtradas = [[valor for valor in columna if valor != '0'] for columna in columnas]
        self.matriz_esquema = columnas_filtradas
        #print(self.matriz_esquema)
        return self.matriz_esquema
    
    def esquema_Grap(self, lista):
        lista = self.matriz_esquema
        graphviz_code = "digraph G {\n"
        # Definimos un nodo para cada elemento de la lista de listas
        for sublist in lista:
            line = " -> ".join(sublist)
            graphviz_code += f'"{line}" \n'
        graphviz_code += "}"
        return graphviz_code
    
    def render_Esquema(self):
        lista = self.convert_esquema()
        total_sublistas = len(lista)
        sublista_por_imagen = 15  # Número de sublistas por imagen
        total_imagenes = total_sublistas // sublista_por_imagen + (total_sublistas % sublista_por_imagen > 0)
        # Iterar sobre el rango de imágenes
        for i in range(1, total_imagenes + 1):
            graph = Digraph()

            # Configuración del estilo de los nodos como cuadrados (boxes)
            graph.attr('node', shape='box')

            # Calcular el rango de sublistas para esta imagen
            start_index = i * sublista_por_imagen
            end_index = min((i + 1) * sublista_por_imagen, total_sublistas)

            # Agregar nodos para cada sublista en el rango
            for sublist_index in range(start_index, end_index):
                line = " => ".join(lista[sublist_index])
                graph.node(line)

            # Agregar conexiones entre las sublistas adyacentes
            for j in range(start_index, end_index - 1):
                graph.edge(" => ".join(lista[j]), " => ".join(lista[j + 1]), style='dashed')

            # Definir la ruta de la imagen
            nombre_imagen = f"Esquema_CRS_{i}.png"
            ruta_completa = os.path.join("Tarea 4", "source", nombre_imagen)

            # Renderizar la imagen
            graph.render(filename=ruta_completa, format="png", view=False, cleanup=True)

def main():
    matrix = SparseMatrix()
    while True:
        print("\n1. Cargar datos desde archivo CSV")
        print("2. Ingresar datos manualmente")
        print("3. Mostrar datos de la matriz dispersa")
        print("4. Generar representación visual de la matriz dispersa")
        print("5. Salir")
        choice = input("Ingrese su opción: ")

        if choice == '1':
            filename = input("Ingrese la ruta del archivo CSV: ")
            matrix.leer_csv(filename)
            if matrix.matriz_esquema == []:
                matrix.convert_esquema()
        elif choice == '2':
            print("¡Hasta luego!")
        elif choice == '3':
            grap = matrix.esquema_Grap(matrix.matriz_esquema)
            print (grap)
        elif choice == '4':
            matrix.render_Esquema()
        elif choice == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
