from ds2.mapping import Mapping, Entry

class ListMapping(Mapping):
    """
    Implements the Mapping abstract base class using a list.
    """

    def __init__(self):
        """
        Initializes a new ListMapping instance with an empty list of entries.
        """
        self._entries = []

    def put(self, key, value):
        """
        Associates the given key with the given value. If the key already exists, updates its value.

        Args:
            key: The key to add or update in the mapping.
            value: The value to associate with the given key.
        """
        e = self._entry(key)
        if e is not None:
            e.value = value
        else:
            self._entries.append(Entry(key, value))

    def get(self, key):
        """
        Retrieves the value associated with the given key.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the given key.

        Raises:
            KeyError: If the key is not found in the mapping.
        """
        e = self._entry(key)
        if e is not None:
            return e.value
        else:
            raise KeyError

    def _entry(self, key):
        """
        Retrieves the Entry associated with the given key.

        Args:
            key: The key to retrieve the Entry for.

        Returns:
            The Entry associated with the given key, or None if not found.
        """
        for e in self._entries:
            if e.key == key:
                return e
        return None

    def _entryiter(self):
        """
        Returns an iterator over the entries in the mapping.

        Returns:
            An iterator over the entries in the mapping.
        """
        return iter(self._entries)

    def __len__(self):
        """
        Returns the number of entries in the mapping.

        Returns:
            int: The number of entries in the mapping.
        """
        return len(self._entries)