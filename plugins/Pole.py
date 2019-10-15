import math
import timeit


def fibonnaci_explicit(n):
    return ((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / (2 ** n * math.sqrt(5))


def fibonnaci_iterative(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


def fibonnaci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonnaci_recursive(n - 1) + fibonnaci_recursive(n - 2)


n =1

start_time = timeit.default_timer()
print(fibonnaci_explicit(n))
print('explicit ' + str(timeit.default_timer() - start_time))

start_time = timeit.default_timer()
print(fibonnaci_iterative(n))
print('iterative ' + str(timeit.default_timer() - start_time))

start_time = timeit.default_timer()
print(1)
print('recursive ' + str(timeit.default_timer() - start_time))