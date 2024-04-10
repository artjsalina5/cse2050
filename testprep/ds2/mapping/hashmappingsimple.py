from ds2.mapping import ListMapping

class HashMappingSimple:
    """
    A simple implementation of a hash map for key-value pairs.
    It uses a Python list as a bucket which stores instances of the `ListMapping` class.
    """

    def __init__(self):
        """
        Initializes a new `HashMappingSimple` instance with a fixed number of buckets.
        """
        self._size = 100  # set size of the hash table
        self._buckets = [ListMapping() for i in range(self._size)]  # create a list of `ListMapping` instance as buckets

    def put(self, key, value):
        """
        Associates the given key with the given value in the Hash Map.

        Args:
            key: The key to be put into hash map.
            value: The value to be associated with the key.
        """
        m = self._bucket(key)  # get the bucket corresponding to the key
        m[key] = value  # put the key-value pair in bucket

    def get(self, key):
        """
        Retrieves the value associated with the given key from the hash map.

        Args:
            key: The key to get the value for from the hash map.

        Returns:
            The value associated with the given key.
        """
        m = self._bucket(key)  # get the bucket corresponding to key
        return m[key]  # return the value associated with the key

    def _bucket(self, key):
        """
        Computes the hash of the key and maps it to a corresponding bucket.

        Args:
            key: The key to find bucket for.

        Returns:
            The bucket which could contain the given key.
        """
        # Here, we assume the key can be hashed and is in the bucket corresponding to `hash(key) % self._size`
        return self._buckets[hash(key) % self._size]