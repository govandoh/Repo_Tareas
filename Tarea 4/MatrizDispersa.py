import csv
from graphviz import Digraph

class SparseMatrix:
    def __init__(self):
        self.data = []
        self.row = []
        self.col = []
        self.column_names = ['age','anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','sex','smoking','time', 'DEATH_EVENT']

    def load_from_csv(self, filename):
        column_names = self.column_names
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            start_row = max(self.row) + 1 if self.row else 0
            for i, row in enumerate(reader):
                for key, value in row.items():
                    if key == 'age':
                        age = float(value)
                        age = round(age)
                        self.row.append(i + start_row)
                        self.col.append(column_names.index(key))
                        self.data.append(age)
                    elif float(value) != 0:
                        self.row.append(i + start_row)
                        self.col.append(column_names.index(key))
                        self.data.append(float(value))

    
    def manually_enter_data(self):
        while True:
            start_row = max(self.row) + 1 if self.row else 0
            print("Ingrese los nuevos datos a agregar a la matriz dispersa:")
            print(f"La siguiente fila disponible es la {start_row}")
            self.row += [start_row] * len(self.column_names)
            self.col += list(range(len(self.column_names)))
            print(f"Ingrese los valores para {len(self.column_names)} columnas (presione enter después de ingresar cada valor):")
            for j in range(len(self.column_names)):
                value = float(input(f"Ingrese el valor para {self.column_names[j]}: "))
                self.data.append(value)
            print("\n¿Desea ingresar más datos manualmente?")
            option = input("Ingrese 'si' para continuar ingresando datos o cualquier otra tecla para volver al menú principal: ")
            if option.lower() != 'si':
                break
    
    def display_ccs(self):
        num_cols = len(self.column_names)
        indptr = [0] * (num_cols + 1)
        for j in self.col:
            indptr[j + 1] += 1
        for i in range(1, len(indptr)):
            indptr[i] += indptr[i - 1]
        # Imprime los datos en el formato (fila, columna): valor
        for r, c, v in zip(self.row, self.col, self.data):
            print(f"({r}, {c}): {v}")


    def generate_graph(self):
        dot = Digraph(comment='Sparse Matrix', format='png')

        num_rows = max(self.row) + 1 if self.row else 0
        num_cols = len(self.column_names)
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
            matrix.display_ccs()
        elif choice == '4':
            matrix.generate_graph()
        elif choice == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
