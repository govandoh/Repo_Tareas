class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def search_by_key(self, key):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def search_by_value(self, value):
        results = []
        for bucket in self.table:
            for k, v in bucket:
                if v == value:
                    results.append((k, v))

        return results

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

    # Inserción manual
    ht.insert("key1", "value1")
    ht.insert("key2", "value2")
    ht.insert("key3", "value3")

    # Mostrar tabla hash
    ht.display()

    # Búsqueda por clave
    print("\nBúsqueda por clave 'key1':", ht.search_by_key("key1"))

    # Búsqueda por valor
    print("\nBúsqueda por valor 'value2':", ht.search_by_value("value2"))

    # Cargar datos desde un archivo CSV
    #ht.load_from_csv('data.csv')
    #ht.display()
