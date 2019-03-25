"""
Given a string, find the length of the longest substring without repeating characters.
"""

"""
Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.
"""

def lengthOfLongestSubstring(s: str) -> int:
    letter_locs = {}
    cur, best, from_ind = 0, 0, 0
    for i, l in enumerate(s):
        if l in letter_locs:
            from_ind = from_ind if from_ind > letter_locs[l] else letter_locs[l]
            cur = i - from_ind
        else:
            cur += 1
        letter_locs[l] = i
        best = cur if cur > best else best
    return best


print(lengthOfLongestSubstring("abccbade"))
print(lengthOfLongestSubstring("abba"))
print(lengthOfLongestSubstring(""))

