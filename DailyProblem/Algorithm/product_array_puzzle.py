"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def generators(nums):  # O(4n)
    """
    Creates 2 generators to iterate through nums forward or backwards based on step keyword
    Performs both passes from left and right of nums in the product list in a single list comprehension
    """
    def gen(step=1, x=1):
        for n in nums[::step]:
            yield x
            x *= n

    g1, g2 = gen(), gen(-1)
    return [next(g2) * p for p in [x for x in g1][::-1]][::-1]


def optimized_prod(nums):  # O(3n)
    """
    Optimized version of left_and_right
    Does 2 passes on the product list rather than initializing separate left and right side lists
    """
    x = 1
    prod = []
    for n in nums:
        prod.append(x)
        x *= n
    x = 1
    for i, n in list(enumerate(nums))[::-1]:
        prod[i] *= x
        x *= n

    return prod


def left_and_right(nums):  # O(6n)
    """
    Construct a temporary lists left, right such that left/right[i] contains product of all elements on left/right
    of nums[i] excluding nums[i].
    To get the product at i (excluding element at i) multiply left[i] by right[i]
    """
    left, right = [1], [1 for _ in nums]  # left only needs initial value, but right must be initialized fully
    enum = list(enumerate(nums))  # iterable and subscript-able

    for i, n in enum[1:]:
        left.append(nums[i-1] * left[-1])
    for i, n in enum[:-1][::-1]:
        right[i] = nums[i+1] * right[i+1]

    return [left[i] * right[i] for i, _ in enum]


def without_division(nums):  # O[(n^2 + n) /2]
    result = [1]
    for n in nums:
        result = [n*r for r in result] + [result[0]]
    return result[1:]


def with_division(nums):  # O(2n)
    """
    Get a grand multiplication total from all elements of the list
    Get the resulting list by dividing by each element at its index
    """
    # Recursive Lambda - multiplication equivalent of sum()
    product = lambda x: x[0] * product(x[1:]) if x[1:] else x[0]
    total = product(nums)
    return [total // n for n in nums]


def brute_force(nums):  # O(n^2)
    result = []
    for i in range(len(nums)):
        sum = 1
        for j in range(len(nums)):
            sum *= nums[j] if j != i else 1
        result.append(sum)
    return result


test1 = [1, 2, 3, 4, 5]
test2 = [5, 3, 6, 1]
test3 = [2, 4, 6, 8]
test4 = [3]

functions = [brute_force, with_division, without_division, left_and_right, optimized_prod, generators]
tests = [test1, test2, test3, test4]

for i in functions:
    print("\n", i.__name__)
    for j in tests:
        print(i(j))
