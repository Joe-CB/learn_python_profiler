from memory_profiler import profile


# Decorator
# @profile(precision=4)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

my_func()


# Time-based memory usage
