from ds2.mapping import Mapping, ListMapping


class HashMapping(Mapping):
    """
    Implements the Mapping abstract base class using a hash table.
    """

    def __init__(self, size=100):
        """
        Initializes a new HashMapping instance with the specified number of buckets.

        Args:
            size (int): The initial number of buckets in the hash table.
        """
        self._size = size
        self._buckets = [ListMapping() for i in range(self._size)]
        self._length = 0

    def _entryiter(self):
        """
        Returns an iterator over the entries in the hash table.

        Returns:
	        An iterator that iterates over every entry in each bucket of the hash table.
        """
        return (e for bucket in self._buckets for e in bucket._entryiter())

    def get(self, key):
        """
        Retrieves the value associated with the given key.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the given key.
        """
        bucket = self._bucket(key)
        return bucket[key]

    def put(self, key, value):
        """
        Associates the given key with the given value. If the key already exists, updates its value.

        Args:
            key: The key to add or update in the mapping.
            value: The value to associate with the given key.
        """
        bucket = self._bucket(key)
        if key not in bucket:
            self._length += 1
        bucket[key] = value

        # Check if we need more buckets.
        if self._length > self._size:
            self._double()

    def __len__(self):
        """
        Returns the number of entries in the hash table.

        Returns:
            int: The number of entries in the hash table.
        """
        return self._length

    def _bucket(self, key):
        """
        Retrieves the bucket for the given key.

        Args:
            key: The key to find the bucket for.

        Returns:
            The bucket that should contain the given key.
        """
        return self._buckets[hash(key) % self._size]

    def _double(self):
        """
        Expands the hash table by doubling its size and rehashing all entries.
        """
        # Save the old buckets
        oldbuckets = self._buckets
        # Reinitialize with more buckets.
        self.__init__(self._size * 2)
        for bucket in oldbuckets:
            for key, value in bucket.items():
                self[key] = value


def test_hash_mapping():
    # Initialize HashMapping with a specific size
    mapping = HashMapping(2)

    # Test put method
    mapping.put("key1", "value1")
    mapping.put("key2", "value2")

    print(f"Size of Mapping: {len(mapping)}")  # Output => Size of Mapping: 2

    # Test get method
    print(mapping.get("key1"))  # Output => value1
    print(mapping.get("key2"))  # Output => value2

    # Test put method for updating existing key
    mapping.put("key1", "new_value1")
    print(mapping.get("key1"))  # Output => new_value1

    # Print all entries in the hash table
    for entry in mapping._entryiter():
        print(entry)


# Running test function
test_hash_mapping()
