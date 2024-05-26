class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        bucket.append((key, value))
        print(f"Insertado: clave = {key}, valor = {value}, hash = {hash_index}")

    def search_by_key(self, key):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        results = [v for k, v in bucket if k == key]
        return results if results else None

    def search_by_value(self, value):
        results = []
        for bucket in self.table:
            results.extend([(k, v) for k, v in bucket if v == value])
        return results if results else None

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")

    def load_from_csv(self, file_path):
        import csv
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if len(row) == 2:
                    self.insert(row[0], row[1])

if __name__ == "__main__":
    ht = HashTable()

    while True:
        print("\n--- Menú ---")
        print("1. Insertar manualmente")
        print("2. Buscar por clave")
        print("3. Buscar por valor")
        print("4. Mostrar tabla hash")
        print("5. Cargar datos desde CSV")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            key = input("Ingrese la clave: ")
            value = input("Ingrese el valor: ")
            ht.insert(key, value)

        elif opcion == '2':
            key = input("Ingrese la clave para buscar: ")
            result = ht.search_by_key(key)
            if result:
                print(f"Valor encontrado para la clave '{key}': {result}")
            else:
                print("Clave no encontrada.")

        elif opcion == '3':
            value = input("Ingrese el valor para buscar: ")
            results = ht.search_by_value(value)
            if results:
                print(f"Resultados encontrados para el valor '{value}': {results}")
            else:
                print("Valor no encontrado.")

        elif opcion == '4':
            ht.display()

        elif opcion == '5':
            file_path = input("Ingrese la ruta del archivo CSV: ")
            ht.load_from_csv(file_path)

        elif opcion == '6':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
