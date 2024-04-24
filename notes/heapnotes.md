In order to talk about Heaps, we must talk about Priority Queues:
Priority Queue: implements a set "S" of elements, associated with a key. This key can be considered the
	"Priority"
	Some basic operations for the Priority Queue that we will build upon later are:
		Insert (S,x): Insert elemeent x into set S. It will get assigned a priority key
		max(S): return max Key "Max Priority"
		extract_max(S): returns max Key AND removes it from S.
		increase_key(S,x,k): increase the value of X's key to a higher one. "Upps the priority"
Heap: An implementation of a Priority Queue. It is an array structure (a list in python), but it is a nearly complete binary tree
Ex: Given the array: [16, 14, 10, 8, 7, 9, 3, 2, 4, 1] 
We must visualize this as a Tree. Our root is index 0. 
    Some basic parameters of a Heap are:
    Root: First element array[i]
    parent(i) = i / 2
    left child(i) = 2 * i
    right_child(i) = (2 * i) - 1
Max Heap Property: the key of a node is >= children's keys. Or in this case, the PRIORITY is what is higher.
    max(S): is trivial in this case, it is the node
    extract_max(S): This is difficult as we need to maintain the max_heap invariant of such that the root is the highest     priority.
How are we going to builld a max_heap out of an unsorted array?

Heap Methods:
    build_max_heap(): produces a max_heap from an unsorted array.
    max_heapify(A[],i): corrects a single violation of the heap invariant in a subtree's root.
        Assume that the tree is rooted at left(i) and righti) are max_heaps.

    for an example, index 2 is out of order. We call max_heapify(A[], 2)
    This is where we want to know what the heap_size is. 
    For this example it is 10.
    Lets look at index 2 in its own little array.
    
    [4, 14, 7, 2, 8, 1]
   
    This is definitely not sorted!
    
    Heapify exchanges A[2] with A[4] (the left child)

    [14, 4, 7, 2, 8, 1]

    Heapify now looks at 4 and its children, 2 and 8. 2 works, but 8 does not, so we flip 4 and 8.

    [14, 8, 7, 2, 4, 1]

    This continues until we have a max_heap.

    What is the complexity of these operations?
    The height is bounded by logn.
    

Convert A[n] into a max_heap
    build_max_heap(A)
        n = heap_size
        for i = n / 2 to n = 1  //elements A[(n/2)+1] are our leafs.
            max_heapify(A,i)   // The reason this works is because every time we are calling this recursively, we are sa                                    tisfying the max_heap invariant recursively.

    Essentially the heapify operation checks the size of the downstream branch and compares the weight. If -1 <= x <= 1 balanced
