"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))
"""


class Solution(object):
    def merge(self, nums1, nums2):

        if not nums1 and not nums2:
            return []
        if not nums1:
            return nums2
        if not nums2:
            return nums1

        merged_array = []
        n1_iter = iter(nums1)
        n2_iter = iter(nums2)

        n1 = next(n1_iter, None)
        n2 = next(n2_iter, None)

        while n1 and n2:
            if n1 <= n2:
                merged_array.append(n1)
                n1 = next(n1_iter, None)
            else:
                merged_array.append(n2)
                n2 = next(n2_iter, None)

        while n1:
            merged_array.append(n1)
            n1 = next(n1_iter, None)

        while n2:
            merged_array.append(n2)
            n2 = next(n2_iter, None)

        return merged_array

    def find_median(self, nums) -> float:
        if len(nums) == 1:
            return float(nums[0])

        middle_index = len(nums) // 2

        if len(nums) % 2 == 0:
            middle_n1 = nums[middle_index]
            middle_n2 = nums[middle_index - 1]
            median = (middle_n1 + middle_n2) / 2
            return float(median)
        else:
            return float(nums[middle_index])

    def remove_min(self, nums1, nums2):
        if nums1[0] <= nums2[0]:
            nums1.pop()
            return nums1, nums2
        else:
            nums2.pop()
            return nums1, nums2

    def reduce_both(self, nums1, nums2):
        while len(nums1) > 2 and len(nums2) > 2:
            nums1_median = self.find_median(nums1)
            nums2_median = self.find_median(nums2)
            if nums1_median == nums2_median:
                return nums1_median
            if nums1_median < nums2_median:
                nums1 = nums1[len(nums1) // 2:]
                nums2 = nums2[:(len(nums2) // 2)]
            if nums1_median > nums2_median:
                nums1 = nums1[:(len(nums1) // 2)]
                nums2 = nums2[len(nums2) // 2:]
        return nums1, nums2

    def reduce_larger(self, nums1, nums2):
        if len(nums1) == len(nums2):
            return nums1, nums2
        if len(nums1) > len(nums2):
            (big_list, small_list) = (nums1, nums2)
        else:
            (big_list, small_list) = (nums2, nums1)

        small_list_median = self.find_median(small_list)
        while len(big_list) > 3:
            big_list_median = self.find_median(big_list)

            if big_list_median <= small_list_median:
                big_list = big_list[len(big_list) // 2:]
            else:
                big_list = big_list[:len(big_list) // 2]
        return big_list, small_list

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        at_least_one_is_empty = not (nums1 and nums2)
        if at_least_one_is_empty or (len(nums1) == 1 and len(nums2) == 1):
            return self.find_median(nums1 + nums2)

        # If we get here, the lists are 'mixed' and non-empty,
        # so we can't just union them.
        total_len_is_even = (len(nums1) + len(nums2)) % 2 == 0
        (nums1, nums2) = self.reduce_both(nums1, nums2)
        (nums1, nums2) = self.reduce_larger(nums1, nums2)
        reduced_len_is_even = (len(nums1) + len(nums2)) % 2 == 0

        if not total_len_is_even == reduced_len_is_even:
            (nums1, nums2) = self.remove_min(nums1, nums2)
        return self.find_median(self.merge(nums1, nums2))
