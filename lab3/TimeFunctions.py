import time


def time_function(func, arg, n_trials=10):
    """Takes a function and argument input and
    will keep track of the results of all n_trials and
    return the minimum amount of execution time as float"""
    min_time = float('inf')
    for i in range(n_trials):
        start_time = time.time()
        func(arg)
        end_time = time.time()
        min_time = min(min_time, end_time - start_time) # Minimum Time modification
    return min_time

def time_function_flexible(func, args_list, n_trials=10):
    """Takes a function and list of elements input and
    will keep track of the results of all n_trials and
    return the minimum amount of execution time as float"""
    min_time = float('inf')
    for i in range(n_trials):
        start_time = time.time()
        func(*args_list)
        end_time = time.time()
        min_time = min(min_time, end_time - start_time) # Minimum Time modification
    return min_time
