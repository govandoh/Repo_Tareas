import csv
from graphviz import Digraph

class SparseMatrix:
    def __init__(self):
        self.data = []
        self.row = []
        self.col = []

    def load_from_csv(self, filename):
        column_names = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction']
        self.row = []
        self.col = []
        self.data = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for key, value in row.items():
                    if key != 'age' and float(value) != 0:
                        self.row.append(int(row['age']) - 1)
                        self.col.append(column_names.index(key) - 1)
                        self.data.append(float(value))
    
    def manually_enter_data(self):
        print("Ingrese los datos de la matriz dispersa:")
        m = int(input("Número de filas: "))
        n = int(input("Número de columnas: "))
        self.row = []
        self.col = []
        self.data = []
        print("Ingrese los valores (presione enter después de ingresar cada valor):")
        for i in range(m):
            for j in range(n):
                value = float(input(f"Valor en la posición ({i+1},{j+1}): "))
                if value != 0:
                    self.row.append(i)
                    self.col.append(j)
                    self.data.append(value)
    
    def display_data(self):
        print("Datos de la matriz dispersa:")
        for i in range(len(self.row)):
            print(f"({self.row[i]}, {self.col[i]}): {self.data[i]}")

    def generate_graph(self):
        dot = Digraph(comment='Sparse Matrix', format='png')

        num_rows = max(self.row) + 1
        num_cols = max(self.col) + 1
        rows = [[] for _ in range(num_rows)]

        for i in range(len(self.row)):
            rows[self.row[i]].append((self.col[i], self.data[i]))

        for i, row in enumerate(rows):
            row.sort(key=lambda x: x[0])
            dot.node(f'r{i}', f'Row {i}')
            for j, val in row:
                dot.node(f'c{j}', f'Col {j}')
                dot.edge(f'r{i}', f'c{j}', label=str(val))
        
        dot.render('sparse_matrix', view=True)

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
            matrix.load_from_csv(filename)
        elif choice == '2':
            matrix.manually_enter_data()
        elif choice == '3':
            matrix.display_data()
        elif choice == '4':
            matrix.generate_graph()
        elif choice == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

