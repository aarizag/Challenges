"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
from typing import List


def two_sum(nums: List[int], target: int) -> bool:
    diffs = set()
    for n in nums:
        if n in diffs:
            return True
        diffs.add(target-n)
    return False


def two_sum_lambda(nums: List[int], target: int) -> bool:
    def add(self, x):
        self.add(x)
        return self
    res = lambda x, num_set: True if target - x[0] in num_set else x[1:] != [] and res(x[1:], add(num_set, x[0]))
    return res(nums, set())


def two_sum_recursive(nums: List[int], target: int) -> bool:
    def inner(ns, s):
        if not ns:
            return False
        s.add(ns[0])
        return target-ns[0] in s or inner(ns[1:], s)
    return inner(nums, set())


print(two_sum([10, 15, 3, 7], 17))
print(two_sum(list(range(25)), 50))
print(two_sum([4, 9, 19, 18, 2], 27))

print(two_sum_lambda([10, 15, 3, 7], 17))
print(two_sum_lambda(list(range(25)), 50))
print(two_sum_lambda([4, 9, 19, 18, 2], 27))

