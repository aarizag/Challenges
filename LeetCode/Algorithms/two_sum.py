from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i, n in enumerate(nums):
            val = target - n
            if n in diffs:
                return [diffs[n], i]
            diffs[val] = i

print(Solution().twoSum([2,7,10,5,9], 9))
