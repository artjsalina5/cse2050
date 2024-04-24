# bucket_search.py

# Introduction to Mapping and Hashing with Bucket Search in Python

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key} : {self.value}"

class MapADT:
    def __init__(self):
        self._entries = []

    def put(self, key, value):
        for e in self._entries:
            if e.key == key:
                e.value = value
                return
        self._entries.append(Entry(key, value))

    def get(self, key):
        for e in self._entries:
            if e.key == key:
                return e.value
        raise KeyError("Key not found: " + str(key))

    def __len__(self):
        return len(self._entries)

    def __contains__(self, item):
        return any(entry.key == item for entry in self._entries)

    def values(self):
        return (e.value for e in self._entries)

    def items(self):
        return ((e.key, e.value) for e in self._entries)


class HashMapping:
    def __init__(self, size=10):
        self._size = size
        self._buckets = [MapADT() for _ in range(self._size)]

    def _hash(self, key):
        return hash(key) % self._size

    def put(self, key, value):
        bucket = self._buckets[self._hash(key)]
        bucket.put(key, value)

    def get(self, key):
        bucket = self._buckets[self._hash(key)]
        return bucket.get(key)

    def digital_folding(item, bucket_size):
        item_str = str(item)
        pieces = [item_str[i:i + 2] for i in range(0, len(item_str), 2)]

        total = 0
        for piece in pieces:
            total += int(piece)

        return total % bucket_size

    def mid_square_hash(key, hash_table_size):
        key_square = key ** 2
        digits = str(key_square)
        mid_index = len(digits) // 2
        # Extract the middle two digits
        hashed_key = int(digits[mid_index - 1:mid_index + 1])
        return hashed_key % hash_table_size

key = 1234
hash_table_size = 100
print(mid_square_hash(key, hash_table_size))  # Output varies based on the key and table size


# Test map ADT
m = MapADT()
m.put("one", 1)
print(len(m))  # Outputs: 1
print("one" in m)  # Outputs: True

# Test hash mapping
hm = HashMapping()
hm.put("one", 1)
print(hm.get("one"))  # Outputs: 1   