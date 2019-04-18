"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

from string import ascii_lowercase


def positive_number_generator(x=1):
    while True:
        yield x
        x += 1


def decode(message: int) -> [str]:
    mapping = {n: c for n, c in zip(range(1, 27), ascii_lowercase)}


def permutations(num: int) -> [int]:

    return

decode(111)
