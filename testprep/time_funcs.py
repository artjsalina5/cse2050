import time

# Returns time in seconds for func(arg) to run
def time_func(func, arg):
    start = time.time()
    func(arg)
    return time.time() - start
