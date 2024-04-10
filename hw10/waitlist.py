#waitlist.py
from datetime import datetime
class Entry:
    def __init__(self, item, priority):
        self.priority = priority
        self.item = item

    def __lt__(self, other):
        return self.priority < other.priority

class HeapPQ:
    def __init__(self):
        self._entries = []

    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._upheap(len(self._entries) - 1)

    def _parent(self, i):
        return (i - 1) // 2

    def _children(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        return range(left, min(len(self._entries), right + 1))

    def _swap(self, a, b):
        L = self._entries
        L[a], L[b] = L[b], L[a]

    def _upheap(self, i):
        L = self._entries
        parent = self._parent(i)
        if i > 0 and L[i] < L[parent]:
            self._swap(i, parent)
            self._upheap(parent)

    def findmin(self):
        return self._entries[0].item

    def removemin(self):
        L = self._entries
        item = L[0].item
        L[0] = L[-1]
        L.pop()
        self._downheap(0)
        return item

    def _downheap(self, i):
        L = self._entries
        children = self._children(i)
        if children:
            child = min(children, key = lambda x: L[x])
            if L[child] < L[i]:
                self._swap(i, child)
                self._downheap(child)

    def __len__(self):
        return len(self._entries)

    def _heapify(self):
        n = len(self._entries)
        for i in reversed(range(n)):
            self._downheap(i)
class PriorityQueue(HeapPQ):
    def __init__(self,
                 items = (),
                 entries = (),
                 key = lambda x: x):
        self._key = key
        self._entries = [Entry(i, p) for i, p in entries]
        self._entries.extend([Entry(i, key(i)) for i in items])
        self._itemmap = {entry.item : index
                         for index, entry in enumerate(self._entries)}
        self._heapify()

    def insert(self, item, priority = None):
        if priority is None:
            priority = self._key(item)
        index = len(self._entries)
        self._entries.append(Entry(item, priority))
        self._itemmap[item] = index
        self._upheap(index)

    def _swap(self, a, b):
        L = self._entries
        va = L[a].item
        vb = L[b].item
        self._itemmap[va] = b
        self._itemmap[vb] = a
        L[a], L[b] = L[b], L[a]

    def changepriority(self, item, priority = None):
        if priority is None:
            priority = self._key(item)
        i = self._itemmap[item]
        self._entries[i].priority = priority
        # Assuming the tree is heap ordered, only one will have an effect.
        self._upheap(i)
        self._downheap(i)

    def _remove_at_index(self, index):
        L = self._entries
        self._swap(index, len(L) - 1)
        del self._itemmap[L[-1].item]
        L.pop()
        self._downheap(index)

    def removemin(self):
        item = self._entries[0].item
        self._remove_at_index(0)
        return item

    def remove(self, item):
        self._remove_at_index(self._itemmap[item])

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) > 0:
            return self.removemin()
        else:
            raise StopIteration

class WaitList:
    def __init__(self):
        self.pq = PriorityQueue(key=self._reservation_priority)

    def _reservation_priority(self, reservation):
        reservation_time = datetime.strptime(reservation['time'], '%H:%M')
        # In the priority tuple, the time comes first, then the name for tiebreaking
        return (reservation_time, reservation['name'])

    def add_customer(self, name, time):
        try:
            datetime.strptime(time, '%H:%M')  # Validate time format
            reservation = {'name': name, 'time': time}
            self.pq.insert(reservation)
            print(f"{name} has been added to the waitlist at {time}")
        except ValueError:
            print("Invalid time format. Please use HH:MM format.")

    def seat_customer(self):
        if len(self.pq) > 0:
            customer = self.pq.removemin()
            print(f"Seating {customer['name']} with a reservation at {customer['time']}")
        else:
            print("No customers to seat.")

    def change_reservation(self, name, new_time):
        # Note: This will require a custom implementation as the PriorityQueue
        # does not support direct updating by key. You would need to remove
        # and re-insert the item or use another method to update.
        # This is a placeholder for the function.
        print("Change reservation functionality needs to be implemented.")

    def peek_next_customer(self):
        if len(self.pq) > 0:
            customer = self.pq.findmin()
            print(f"The next customer on the waitlist is: {customer['name']}, reservation time: {customer['time']}")
        else:
            print("No customers in the waitlist.")

    def print_reservation_list(self):
        print("Current reservation list:")
        for customer in self.pq:
            print(f"{customer['name']} at {customer['time']}")
