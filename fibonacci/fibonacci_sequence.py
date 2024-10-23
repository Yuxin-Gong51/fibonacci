import fibonacci


def fib_seq(n):
    if n == 0:
        return [0]
    else:
        return fib_seq(n - 1) + [fibonacci.fib(n)]
