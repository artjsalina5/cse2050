# Priority Queues

We're going to discuss a versatile and  fundamental data structure called a **priority queue**.  It will resemble a queue except that items all have a priority and will come out ordered by their priority rather than their order of insertion.

By this point, we know enough about different data structures that we will be able to implement this data structure in several different ways.  Eventually, we will introduce a data structure called a **heap** that will give good performance in many respects.

## The Priority Queue ADT

The **Priority Queue ADT** is a data type that stores a collection of items with priorities (not necessarily unique) that supports the following operations.

  - `insert(item, priority)` - Add `item` with the given `priority`.

  - `findmin()` - Return the item with the minimum priority.  If there are multiple items with the minimum priority, ties may be broken arbitrarily.

  - `removemin()` - Remove and return the item with the minimum priority.  Ties are broken arbitrarily.

## Using a list

As with every ADT presented in this book, there is a simple, though not necessarily efficient, implementation using a list. Let's start with a list and put all the entries in the list. To find the min, we can iterate through the list.

```python {cmd id="_priorityqueue.simplelistpq"}
class SimpleListPQ:
    def __init__(self):
        self._L = []

    def insert(self, item, priority):
        self._L.append((item, priority))

    def findmin(self):
        return min(self._L, key = lambda x : x[1])[0]

    def removemin(self):
        item, priority = min(self._L, key = lambda x : x[1])
        self._L.remove((item, priority))
        return item
```

Although this code will work, there are a couple design decisions that are not great. First, there is something we might call *magical indices*.
As the data are stored as tuples, we have to use an index to pull out the priority or the item as needed.  This is an undocumented convention.  Someone reading the code would have to read the insert code to understand the `findmin` code. Also, there is some duplication in the use of `min` with the same `key` lambda expression for both `removemin` and `findmin`. These shortcomings can be our motivation to go back and clean it up, i.e. **refactor** it.

We'll make a class that stores the entries, each will have an `item` and a `priority` as attributes. We'll make the entries comparable by implementing `__lt__` and thus the comparison of entries will always just compare their priorities.

```python {cmd id="_priorityqueue.entry"}
class Entry:
    def __init__(self, item, priority):
        self.priority = priority
        self.item = item

    def __lt__(self, other):
        return self.priority < other.priority
```

Now, we can rewrite the list version of the priority queue.  It's almost the same as before, except, that by using the `Entry` class, the code is more explicit about the types of objects, and hopefully, easier to read and understand.

```python {cmd id="_priorityqueue.unsortedlistpq"}
from ds2.priorityqueue import Entry

class UnsortedListPQ:
    def __init__(self):
        self._entries = []

    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))

    def findmin(self):
        return min(self._entries).item

    def removemin(self):
        entry = min(self._entries)
        self._entries.remove(entry)
        return entry.item
```

Let's analyze the running time of the methods in this class.
The `insert` method will clearly only require constant time because it is a single list append.  Both `findmin` and `removemin` take $O(n)$ time for a priority queue with $n$ items, because the `min` function will iterate through the while list to find the smallest priority entry.

The `findmin` would be much faster if the list were sorted.  Then we could just return the first item in the list.  An even better approach would sort the list backwards.  Then `removemin` could also be constant time, using the constant-time `pop` function on a list.

```python {cmd id="_priorityqueue.sortedlistpq"}
from ds2.priorityqueue import Entry

class SortedListPQ:
    def __init__(self):
        self._entries = []

    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._entries.sort(reverse = True)

    def findmin(self):
        return self._entries[-1].item

    def removemin(self):
        return self._entries.pop().item
```

I used a nice feature of the Python `sort` method, a named parameter called `reversed` which, as one might guess, reverses the sorting order.


```python {cmd continue="_priorityqueue.sortedlistpq"}
S = SortedListPQ()
S.insert("ham", 3)
S.insert("cheese", 1)
S.insert("bread", 2)
print([S.removemin() for i in [1,2,3]])
```

The asymptotic running time of both `findmin` and `removemin` is reduced to constant-time.  The `insert` method no longer runs in constant time, because it sorts.  This means that the running time will depend on the time it takes to sort.  In this case, assuming no other methods rearrange the (private!) `_entries` attribute, there will be only one entry out of sorted order, the one we just appended.  In this case, a good implementation of insertion sort would run in linear time (it only has to insert one item before everything is sorted).  Although, for code brevity, we called out to Python's `sort` method, (which could take $O(n \log n)$-time) this is really a linear-time operation).

What we have with our two list implementations of the priority queue ADT is **tradeoff** between two operations.  In one case, we have fast `insert` and slow `removemin` and in the other we have slow `insert` and fast `removemin`.  Our goal will be to get all of the operations pretty fast.  We may not achieve constant time for all, but logarithmic-time is achievable.

## Heaps

The data structure we'll use for an efficient priority queue is called a **heap**.  Heaps are almost always used to implement a priority queue so that as you look at other sources, you might not see a distinction between the two ideas.  As we are using it, the priority queue is the ADT, the heap is the data structure.  

Matters are complicated by two other vocabulary issues.  First, there are many different kinds of heaps.  We'll study just one example, the so-called binary heap.  Second, the usual word used for the *priority* in a heap is "key".  This can be confusing, because unlike *keys* in mapping data structures, there is no requirement that priorities be unique.  We will stick with the word "priority" despite the usual conventions in order to keep these ideas separate.

We can think of a binary heap as a binary tree that is arranged so that smaller priorities are above larger priorities.  The name is apt as any good heap of stuff should have the big things on the bottom and small things on the top.  For any tree with nodes that have priorities, we say that the **tree is heap-ordered** if for every node, the priority of its children are at least as large as the priority of the node itself.  This naturally implies that the minimum priority is at the root.

## Storing a tree in a list

Previously, we stored trees as a **linked data structure**.  This means having a node class that stores references to other nodes, i.e. the children.  We'll use the heap as an opportunity to see a different way to represent a tree.  We'll put the heap entries in a list and let the list indices encode the parent-child relationships of the tree.

For a node at index `i`, its left child will be at index `2 * i + 1` and the right child will be at index `2 * i + 2`.  This means that the parent of the node at index `i` is at index `(i-1) // 2`.  This mapping of nodes to indices puts the root at index `0` and the rest of the nodes appear level by level from left-to-right, top-to-bottom.  Using this mapping, we say a **list is heap-ordered** if the corresponding binary tree is heap-ordered.  This is equivalent to saying that for all $i > 0$, the priority of the entry at index $i$ is greater than or equal to the priority at index $(i-1) // 2$.

We will maintain the invariant that after each operation, the list of entries is heap-ordered.  To insert a new node, we append it to the list and then repeated swap it with its parent until it is heap-ordered.  This updating step will be called `_upheap` and is similar to the inner loop of an insertion sort.  However, unlike insertion sort, it only does at most $O(\log n)$ swap operations (each one reduces the index by half).

Similarly, there is a `_downheap` operation that will repeatedly swap an entry with its child until it's heap-ordered.  This operation is useful in the next section for building a heap from scratch.

The main operation used in these methods to rearrange the heap is to swap two items using a method called `_swap`.


```python {cmd id="_priorityqueue.heappq_01"}
from ds2.priorityqueue import Entry

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
```

## Building a Heap from scratch, `_heapify`

Just using the public interface, one could easily construct a `HeapPQ` from a list of item-priority pairs.  For example, the following code would work just fine.

```python {cmd continue="_priorityqueue.heappq"}
pq = HeapPQ()
pairs = [(10, 10), (2, 2), (30, 30), (4,4)]
for item, priority in pairs:
    pq.insert(item, priority)
```

The `insert` method takes $O(\log n)$ time, so the total running time for this approach is $O(n \log n)$ time.  *You should double check that you believe this claim despite the fact that for each insertion, there are fewer than $n$ entries.*

Perhaps surprisingly, we can construct the `HeapPQ` in linear time.  We call this **heapifying a list**.  We will exploit the `_downheap` method that we have already written.  The code is deceptively simple.

```python {cmd id="_priorityqueue.heappq_01" continue="_priorityqueue.heappq_01"}
    def _heapify(self):
        n = len(self._entries)
        for i in reversed(range(n)):
            self._downheap(i)
```

Look at the difference between the `heapify` code above and the `_heapify_slower` code below.  The former works from the end and `downheap`s every entry and the latter starts at the beginning and `upheap`s every entry.  Both are correct, but one is faster.

```python {cmd id="heapify1" continue="_priorityqueue.heappq_01"}
    def _heapify_slower(self):
        n = len(self._entries)
        for i in range(n):
            self._upheap(i)
```

They may seem to be the same, but they are not.  To see why, we have to look a little closer at the running time of `_upheap` and `_downheap`.  Consider the tree perspective of the list.  For `_upheap`, the running time depends on the depth of the starting node.  For `_downheap`, the running time depends on the height of the subtree rooted at the starting node.  Looking at a complete binary tree, half of the nodes are leaves and so `_downheap` will take constant time and `_upheap` will take $O(\log n)$ time.  Thus, `_heapify_slower` will take at least $\frac{n}{2}\log_2 n = O(n \log n)$ time.  

On the other hand, to analyze `_heapify`, we have to add up the heights of all the nodes in a complete binary tree.  Formally, this will be $n\sum_{i=1}^{\log_2 n}i/2^i$.  There is a cute trick to bound this sum.  Simply observe that if from every node in the tree, we take a path that goes left on the first step and right for every step thereafter, no two paths will overlap.  This means that the sum of the lengths of these paths (which is also to the sum of the heights) is at most the total number of edges, $n-1$.  Thus, `_heapify` runs in $O(n)$ time.

## Implicit and Changing Priorities

Sometimes, we would like our priority queue to just compare items, rather than their priorities.
That is, the priority is implicit.
To accomplish this, we can make the priority optional for the methods that use it.
Moreover, we often would like to specify some function `key` such that the priority of `item` should be `key(item)`.
This is, for example how it worked for other functions on ordered collections, like `sort`, `min`, and `max`.
We will take care of both goals at once.
We will allow an optional parameter to `__init__` to specify the key function.
The default value of this function will be a function that takes an item and simply returns that same item.
This way, if no key function is given and no priority is given, the priority will be equal to the item.

There is another standard operation on priority queues.  It is called `changepriority`.  It does what it says, changing the priority of an entry.
This is very simple to implement in our current code if the index of the entry to change is known.
It would suffice to change the priority of the entry and call `_upheap` and `_downheap` on that index.
If it needs to move up the heap to recover the heap order invariant, the `_upheap` method will do that.
If it needs to move down the heap, the `_upheap` method will leave it where it is, and the `_downheap` method will move it down the heap until the heap ordering is recovered.

However, the usual way to change the priority is to specify the item and its new priority.  This requires us to know the index of an item.
We'll do this by storing a dictionary that maps items to indices.
We'll have to update this dictionary every time we rearrange the items.  To make sure this happens correctly, we will add a method for swapping entries and use this whenever we make a swap.  

We will add the ability to initialize the heap with a collection using `_heapify`, setting a `key` function if desired.
The default parameter for initializing will just be a list of items.
If instead, one wants to initialize the heap with a collection of `(item, priority)`-pairs, we will use a keyword argument `entries`.
This full version of the priority queue will be very useful for some graph algorithms that we will see soon.

```python {cmd id="_priorityqueue.priorityqueue_01"}
from ds2.priorityqueue import Entry, HeapPQ

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
```

```python {cmd id="removemin" continue="_priorityqueue.priorityqueue_02"}
    def removemin(self):
        L = self._entries
        item = L[0].item
        self._swap(0, len(L) - 1)
        del self._itemmap[item]
        L.pop()
        self._downheap(0)
        return item
```

We can use the code above to implement a `MaxHeap`, that is a priority queue of items ordered by *decreasing* value.

```python {cmd continue="removemin"}
maxheap = PriorityQueue(key = lambda x: -x)

n = 10
for i in range(n):
    maxheap.insert(i) #no need to specify the priority

# These should print in decreasing order.
print([maxheap.removemin() for i in range(n)])
```

## Random Access

Storing the map from items to their indices allows some other operations on the heap.
For example, we could remove an arbitrary item by using the same approach as in `removemin`.
Instead of working with index `0` (the top of the heap), we instead find the index of the item to remove.
The following code gives the factored version of both `removemin` and `remove`.

```python {cmd id="_priorityqueue.priorityqueue_02" continue="_priorityqueue.priorityqueue_01"}
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
        self.remove_at_index(self._itemmap[item])
```

Note that in some cases, we could do this using the public interface.
For example, if the priorities are numbers, then changing the priority to negative infinity (`float('-inf')`) followed by a `removemin()` operation *might* remove the desired entry.
This assumes there aren't other entries with priority negative infinity.
It's better to not try to be too clever.

## Iterating over a Priority Queue

For many operations that use a priority queue, one wants to get the items one at a time, possibly add new items and then repeat until there is nothing left.
This is a little strange compared to other iterators that we've seen, because it will modify the data structure.
In fact, it will destroy it.
For this reason, we don't want to create an iterator object for the priority queue.
We want the priority queue itself to be an iterator.

Recall that in order to be an iterator, the object must have both an `__iter__` method and a `__next__` method.
The `__iter__` method is supposed to return an iterator, which in this case, is just the priority queue itself.

```python {cmd id="_priorityqueue.priorityqueue_03" continue="_priorityqueue.priorityqueue_02"}
    def __iter__(self):
        return self
```

The `__next__` method will return the next item, assuming there is one.
It also should raise `StopIteration` if there is nothing left.
This will signal the end of a `for` loop for example.

```python {cmd id="_priorityqueue.priorityqueue_04" continue="_priorityqueue.priorityqueue_03"}
    def __next__(self):
        if len(self) > 0:
            return self.removemin()
        else:
            raise StopIteration
```


## Heapsort

We can use a priority queue to sort a list.
We just put all the items into a priority queue and then pull them out again in sorted order.
This method of sorting is traditionally called `heapsort` though it will work with any priority queue.


```python {cmd id="_sorting.heapsort"}
from ds2.priorityqueue import PriorityQueue

def heapsort(L):
    H = PriorityQueue(L)
    L[:] = [item for item in H]
```

```python {cmd continue="_sorting.heapsort"}
L = [3,2,4,1, 6, 5]
print("before heapsort:", L)
heapsort(L)
print("after heapsort: ", L)
```

Is this efficient?
The initialization of the `PriorityQueue` takes only $O(n)$ using our `_heapify` method.
However, the iteration is going to cost us $O(\log n)$ time per item.
Thus, the running time will be $O(n\log n)$ just as in `mergesort` or `quicksort`.
