"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

# [3, 4, -1, 1] -> mul -12, sum 7, mul_pos 12
# [1, 2, 0] -> mul 0, sum 3, mul_pos 2


def positive_number_generator(x=1):
    while True:
        yield x
        x += 1


def non_constant_space(nums):
    num_set = set(nums)
    pos_nums = positive_number_generator()
    for p in pos_nums:
        if p not in num_set:
            return p


def solution(nums):

    pass


t1 = [3, 4, -1, 1]
t2 = [1, 2, 0]
functions = [non_constant_space]
tests = [t1, t2]

for i in functions:
    print("\n", i.__name__)
    for j in tests:
        print(i(j))


