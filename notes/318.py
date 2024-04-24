# mapping_intro.py
# Here is a Python file explaining mappings and hashes.

# === Introduction to Mapping ===

# In a map, you associate a value with a unique key. These associated pairs are referred as key-value pairs.
# Python's built-in mapping data type is the dictionary (or 'dict'). Each key in the dictionary is unique, so each value is associated with a a single, unique key.

# Here's an example of dictionary usage:
my_dict = {'apple': 1, 'banana': 2}
print(my_dict['apple'])  # Outputs: 1

# === Introduction to Hashing ===
# A hash is an integral value computed from key data. Hashing takes the key data and returns an integral value ('hash').

# It's used in hash tables or hash maps which are collections of key-value pairs. The key data is hashed, and the resultant hash directs where the value for that key is stored.

# Hashing example: Python's inbuilt hashing function
print(hash('apple'))  # Outputs: Some number (it varies every session)

# === Buckets in Hash Tables ===
# In hash tables, these pairs (bucket) are stored in such a way that inserting, deleting, and finding values is optimal.

# === Example: Implementation of Mapping Abstract Data Type (ADT) ===

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return str(self.key) + " : " + str(self.value)

class MapADT:
    def __init__(self):
        self._entries = []

    def put(self, key, value):
        e = self._entry(key)
        if e:
            e.value = value
        else:
            self._entries.append(Entry(key, value))

    def get(self, key):
        e = self._entry(key)
        if e:
            return e.value
        else:
            raise KeyError(key)

    def _entry(self, key):
        for e in self._entries:
            if e.key == key:
                return e
        return None

    def remove(self, key):
        e = self._entry(key)
        if e is not None:
            self._entries.remove(e)
    def __len__(self):
        return len(self._entries)
    def __contains__(self, item):
        return any(entry.key == item for entry in self._entries)
    def values(self):
        return (e.value for e in self._entries)

    def items(self):
        return((e.key, e.value) for e in self._entries)

m = MapADT()
m.put(4, 'four')
m.put(1, 'one')
__getitem__ == get
print(m.get(1))  # Outputs: 'one'
print(m.get(4))  # Outputs: 'four'
# print(m.get(3))  # Raises: KeyError

