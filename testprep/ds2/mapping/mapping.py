

class Entry:
    """
    Class to represent a key-value pair.
    """
    def __init__(self, key, value):
        """
        Initializes an Entry with the given key and value.

        Args:
            key: The key for this entry.
            value: The value for this entry.
        """
        self.key = key
        self.value = value

    def __str__(self):
        """
        Returns a string representation of this entry.

        Returns:
            str: A string representation of this entry.
        """
        return str(self.key) + " : " + str(self.value)

class Mapping:
    """
    Class to represent a mapping from keys to values. This is an abstract base class and should not be instantiated directly.
    """
    # Child class needs to implement this!
    def get(self, key):
        raise NotImplementedError

    # Child class needs to implement this!
    def put(self, key, value):
        raise NotImplementedError

    # Child class needs to implement this!
    def __len__(self):
        raise NotImplementedError

    # Child class needs to implement this!
    def _entryiter(self):
        raise NotImplementedError

    def __iter__(self):
        """
        Returns an iterator that allows iterating through the keys in the mapping.

        Returns:
            iterator: An iterator for the keys in the mapping.
        """
        return (e.key for e in self._entryiter())

    def values(self):
        """
        Returns an iterator that allows iterating through the values in the mapping.

        Returns:
            iterator: An iterator for the values in the mapping.
        """
        return (e.value for e in self._entryiter())

    def items(self):
        """
        Returns an iterator that allows iterating through the key-value pairs (as tuples) in the mapping.

        Returns:
            iterator: An iterator for the key-value pairs in the mapping.
        """
        return ((e.key, e.value) for e in self._entryiter())

    def __contains__(self, key):
        """
        Checks if the given key is in the mapping.

        Args:
            key: The key to check for in the mapping.

        Returns:
            bool: True if the key is in the mapping, False otherwise.
        """
        try:
            self.get(key)
        except KeyError:
            return False
        return True

    def __getitem__(self, key):
        """
        Retrieves the value associated with the given key.

        Args:
            key: The key for which to retrieve the value.

        Returns:
            value: The value associated with the given key.
        """
        return self.get(key)

    def __setitem__(self, key, value):
        """
        Associates the given value with the given key.

        Args:
            key: The key with which to associate the value.
            value: The value to associate with the key.
        """
        self.put(key, value)

    def __str__(self):
        """
        Returns a string representation of the mapping.

        Returns:
            str: A string representation of the mapping.
        """
        return "{" + ", ".join(str(e) for e in self._entryiter()) + "}"