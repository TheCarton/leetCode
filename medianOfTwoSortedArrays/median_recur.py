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

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        at_least_one_is_empty = not (nums1 and nums2)
        if at_least_one_is_empty or (len(nums1) == 1 and len(nums2) == 1):
            return self.find_median(nums1 + nums2)

        nums1_max_less_than_nums2_min = nums1[-1] <= nums2[0]
        if nums1_max_less_than_nums2_min:
            return self.find_median(nums1 + nums2)

        nums2_max_less_than_nums1_min = nums2[-1] <= nums1[0]
        if nums2_max_less_than_nums1_min:
            return self.find_median(nums2 + nums1)

        # If we get here, the lists are 'mixed' and non-empty,
        # so we can't just union them.

        nums1_median = self.find_median(nums1)
        if nums1_median <= nums2[0]:
            return self.findMedianSortedArrays(nums1[len(nums1) // 2:], nums2[:len(nums2) // 2])
        if nums1_median >= nums2[-1]:
            return self.findMedianSortedArrays(nums1[:len(nums1) // 2], nums2[len(nums2) // 2:])

        nums2_median = self.find_median(nums2)
        if nums2_median <= nums1[0]:
            return self.findMedianSortedArrays(nums2[len(nums2) // 2:], nums1[:len(nums1) // 2])
        if nums2_median >= nums1[-1]:
            return self.findMedianSortedArrays(nums2[:len(nums2) // 2], nums1[len(nums1) // 2:])
