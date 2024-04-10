class CustomSet:
    def __init__(self):
        """Initializes an empty CustomSet"""
        self._min_buckets = 8  # We never want to rehash down below this many buckets.
        self._n_buckets = 8  # initial size. Good to use a power of 2 here.
        self._len = 0  # Number of items in custom set
        self._L = [[] for i in range(self._n_buckets)]  # List of empty buckets

    def __len__(self):
        """Returns the number of items in CustomSet"""
        return self._len

    def _find_bucket(self, item):
        """Returns the index of the bucket `item` should go in, based on hash(item) and self._n_buckets"""
        return hash(item) % self._n_buckets

    def __contains__(self, item):
        """Returns True if item is in the CustomSet"""
        bucket_index = self._find_bucket(item)
        return item in self._L[bucket_index]

    def add(self, item):
        """Adds a new item to CustomSet. Duplicate adds are ignored."""
        if item not in self:
            bucket_index = self._find_bucket(item)
            self._L[bucket_index].append(item)
            self._len += 1
            if self._len >= 2 * self._n_buckets:
                self._rehash(2 * self._n_buckets)

    def remove(self, item):
        """Removes item from CustomSet. Raises a KeyError if item is not found."""
        if item not in self:
            raise KeyError("Attempt to remove non-extant item {}".format(item))
        bucket_index = self._find_bucket(item)
        self._L[bucket_index].remove(item)
        self._len -= 1
        if self._len <= self._n_buckets / 2 and self._n_buckets / 2 >= self._min_buckets:
            self._rehash(int(self._n_buckets / 2))

    def _rehash(self, new_buckets):
        """Rehashes every item to a new hash table with new_buckets."""
        old_L = self._L
        self._L = [[] for _ in range(new_buckets)]
        self._n_buckets = new_buckets
        self._len = 0  # Reset length and re-add items to reset it accurately
        for bucket in old_L:
            for item in bucket:
                self.add(item)

# Example interactive window usage and expected output
if __name__ == "__main__":
    s = CustomSet()
    print("hello" in s)  # Expected: False
    s.add("hello")
    print(len(s))  # Expected: 1
    print("hello" in s)  # Expected: True
    s.remove("hello")
    try:
        s.remove(5)
    except KeyError as e:
        print(e)  # Expected: Attempt to remove non-extant item 5
