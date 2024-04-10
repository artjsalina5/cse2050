from quad_sorts import bubble, selection, insertion
from time_funcs import time_func
import random

def print_table(title, L, ns):
    print()
    width = 40
    print(title.center(width, "="))
    print("{:10}{:10}{:10}{:10}".format("n", "bubble", "select", "insert"))
    print("-"*width)

    for n in ns:
        print("{:<10}".format(n), end = '')
        print("{:<10.2g}".format(time_func(bubble, L[:n])), end = '')
        print("{:<10.2g}".format(time_func(selection, L[:n])), end = '')
        print("{:<10.2g}".format(time_func(insertion, L[:n])))
    print("-"*width)

ns = [100, 200, 500, 1000, 2000, 5000]

############# Random Distribution ##############
# TODO: Create a list of randomly distributed integers
# L = [random.randint(0,100) for i in range(ns[-1])]
# print_table("Random Distribution", L, ns)



############# 1 item out of place ##############
#### Big item at front
# TODO: Create a mostly sorted list with one big item at the front
#L = [i for i in range(ns[-1])]
#L[0] = 5000
# print_table("Big at front", L, ns)

#### Little item at back
# TODO: Create a mostly sorted list with one little item at the back
#L = [i for i in range(ns[-1])]
#for n in ns:
#    L[n-1] = -1
#print_table("Little at back", L, ns)


############ Reverse Sorted ##############
# TODO: Create a reverse sorted list
L = [i for i in range(ns[-1], -1, -1)]
print_table("Reverse Sorted", L, ns)
