from ds2.mapping import Entry

class ListMappingSimple:
    """
    A simple implementation of a key-value mapping using a list.
    Each entry in the list is an object of the Entry class which contains a key and value.
    """

    def __init__(self):
        """
        Initializes a new ListMappingSimple instance.
        """
        self._entries = []  # a list to store all entries

    def put(self, key, value):
        """
        Associates the given key with the given value. If the key already exists in the mapping, its existing value is updated to the new value.

        Args:
            key: The key to put into the mapping.
            value: The value to associate with the given key.
        """
        for e in self._entries:  # iterate through each entry in the list
            if e.key == key:  # if key already exists in entries
                e.value = value  # update value of the existing key
                return
        self._entries.append(Entry(key, value))  # if key doesn't exist, create a new entry with the given key-value pair

    def get(self, key):
        """
        Retrieves the value associated with the given key.

        Args:
            key: The key to get the value for from the mapping.

        Returns:
            The value associated with the given key.

        Raises:
            KeyError: If the key does not exist in the mapping.
        """
        for e in self._entries:  # iterate through each entry in the list
            if e.key == key:  # if key exists in entries
                return e.value  # return the value of the key

        # if program reaches this point,
        # it means the key was not found in the mapping, thus raise a KeyError
        raise KeyError