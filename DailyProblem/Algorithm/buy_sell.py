"""
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order,
    write a function that calculates the maximum profit you could have made from buying
    and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5,
    since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

# low = 9, high = 9, max = -inf
# low = 9, high = 11, max =2
# low = 8, high = 8 max = 2
# low = 5, high = 5 max = 2
# low = 5, high = 7 max = 2
# low = 5, high = 10 max = 5

def solution(arr):
    low = high = arr[0]
    max = float("-inf")

    for n in arr[1:]:
        if n < low:
            low = high = n
        elif n > high:
            high = n
        max = high-low if high-low > max else max
    return max


print(solution([9, 11, 8, 5, 7, 10]))
print(solution([0, 10, 3, 15, 5, 8]))
print(solution([10, 12, 15, 0, 4, 9, 8]))
