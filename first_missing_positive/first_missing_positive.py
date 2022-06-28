"""
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive/
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
______________________
Maximum is the largest possible positive, which is the length of the list plus one at first.

pos is the first missing positive, which is 1 at first.

The first missing positive must be between pos and maximum.

For each number in nums,

Check if the number is positive. If it isn't, decrement the maximum since we 'wasted' a number.

Check if the number is equal to the first missing positive. If it is, we need to increment the first
missing positive.

Check if the number is less than or equal to the maximum. If it is, we need to push it onto the stack.
Otherwise, decrement the maximum since we 'wasted' a number.


Pushing onto the stack:
If the stack is empty, just insert the new number.

If the

__________________________

Use a heap instead of a stack?
[3, 4, -1, 1]
max = 5
enter loop:
first: 3, less than max. Save it.
second: 4, less than max, more than 3. Save it.
Solution from asones
"""


class Solution(object):
    def firstMissingPositive(self, nums) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(n):
            nums[nums[i] % n] += n
        for i in range(1, n):
            if nums[i] // n == 0:
                return i
        return n
