"""
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive/
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""


class Solution(object):
    @staticmethod
    def find_new_missing(old, a, b) -> int:
        new = old
        if a + 1 < b:
            new = a + 1
        return new

    def firstMissingPositive(self, nums) -> int:
        min_pos, right_missing = None, None
        for n in nums:
            if n < 1:
                continue
            if not min_pos:
                min_pos = n
                right_missing = min_pos + 1
            if n < min_pos:
                right_missing = self.find_new_missing(right_missing, n, min_pos)
                min_pos, next_min_pos = n, min_pos
            if n == right_missing:
                right_missing += 1

        return self.find_new_missing(right_missing, 0, min_pos)
