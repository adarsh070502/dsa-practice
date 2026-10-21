class HashTable:

    def __init__(self, size):
        self.size = size
        self.data_inserted = 0
        self.data = [None] * size

    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % self.size
        return hash_value

    def set(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        if self.data[index] is None:
            # Create a bucket (list) for handling collisions
            self.data[index] = []
        # Check if the key already exists and update its value
        for i, pair in enumerate(self.data[index]):
            if pair[0] == key:
                self.data[index][i] = (key, value)
                return
        # Otherwise, append the new key-value pair
        self.data[index].append((key, value))
        self.data_inserted += 1

    def get(self, key):
        """Retrieve the value associated with the given key."""
        index = self._hash(key)
        if self.data[index] is not None:
            for pair in self.data[index]:
                if pair[0] == key:
                    return pair[1]
        return None  # Return None if the key is not found

    def keys(self):
        all_keys = []

        for ele in self.data:
            if ele is not None:
                for e in ele:
                    all_keys.append(e[0])
        return all_keys

    def print_hash_table(self):
        print(self.data)


myHashTable = HashTable(50)
myHashTable.set('grapes', 10000)
myHashTable.print_hash_table()
print(myHashTable.get('grapes'))
myHashTable.set('apples', 9)
print(myHashTable.get('apples'))
myHashTable.set('oranges', 9)
myHashTable.set('watermelon', 9)
myHashTable.set('mangoes', 9)
print(myHashTable.keys())
