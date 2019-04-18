"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""


def scheduler(f, n):
    from time import sleep
    sleep(n*.001)
    f()


test_func = (lambda: 3+4)
scheduler(test_func, 10)
