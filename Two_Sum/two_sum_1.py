from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_sols = dict()
        for (index, n) in enumerate(nums):
            if n in pos_sols:
                return [index, pos_sols.get(n)]
            pos_sol = target - n
            pos_sols.update({pos_sol: index})
