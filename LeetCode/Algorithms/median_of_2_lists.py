"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""

from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    total_size = len(nums1) + len(nums2)
    midnum = total_size // 2 + 1
    new_list = []
    i, j = 0, 0
    for k in range(midnum):
        if nums1[i] < nums2[j]:
            less = nums1[i]
            i += 1
        else:
            less = nums2[j]
            j += 1
        new_list.append(less)
    return (new_list[-1] + new_list[-2]) / 2 if total_size % 2 == 0 else new_list[-1]


def find_median(nums1, nums2):
    def foo(n1, n2):
        print(f"{n1}   {n2}")
        ln1, ln2 = len(n1), len(n2)
        if ln1 == 1 or ln2 == 1:
            return
        m1, m2 = sum(divmod(ln1, 2)), sum(divmod(ln2, 2))
        if n1[m1] < n2[m2]:
            foo(n1[m1-ln1%2:], n2[:m2])
        else:
            foo(n1[:m1], n2[m2-ln2%2:])
    foo(nums1, nums2)


t1 = [1, 3], [2]
t2 = [1, 3], [2, 4]
t3 = list(range(1, 20, 2)), list(range(2, 19, 2))
t4 = list(range(2,10)), [1,2]

# print(findMedianSortedArrays(*t1))
# print(findMedianSortedArrays(*t2))
print(findMedianSortedArrays(*t3))

find_median(*t4)