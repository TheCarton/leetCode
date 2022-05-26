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

        while n1 is not None and n2 is not None:
            if n1 <= n2:
                merged_array.append(n1)
                n1 = next(n1_iter, None)
            else:
                merged_array.append(n2)
                n2 = next(n2_iter, None)

        while n1 is not None:
            merged_array.append(n1)
            n1 = next(n1_iter, None)

        while n2 is not None:
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
        if not nums1 and not nums2:
            return [], []
        if not nums1:
            nums2.pop(0)
            return [], nums2
        if not nums2:
            nums1.pop(0)
            return nums1, []
        if nums1[0] <= nums2[0]:
            nums1.pop(0)
        else:
            nums2.pop(0)
        return nums1, nums2

    def remove_max(self, nums1, nums2):
        if not nums1 and not nums2:
            return [], []
        if not nums1:
            nums2.pop()
            return [], nums2
        if not nums2:
            nums1.pop()
            return nums1, []
        if nums1[-1] >= nums2[-1]:
            nums1.pop()
        else:
            nums2.pop()
        return nums1, nums2

    def switch_number_to_smaller_list(self, small_list, big_list):
        if big_list[0] >= small_list[-1]:
            small_list.append(big_list.pop(0))
            return small_list, big_list
        else:
            for i, n in enumerate(small_list):
                if big_list[0] <= n:
                    small_list.insert(i, big_list.pop(0))
                    break
        return small_list, big_list

    def order_lists(self, nums1, nums2):
        if len(nums1) >= len(nums2):
            (small_list, big_list) = nums2, nums1
        else:
            (small_list, big_list) = nums1, nums2
        return small_list, big_list

    def balance_large(self, nums1, nums2):
        (small_list, big_list) = self.order_lists(nums1, nums2)
        if len(small_list) == 0:
            small_list = big_list[:len(big_list) // 2]
            big_list = big_list[len(big_list) // 2:]
            return self.order_lists(small_list, big_list)

        i = len(big_list) // 2
        while i < len(big_list):
            if big_list[i] >= small_list[-1]:
                tail = big_list[i:]
                small_list = small_list + tail
                big_list = big_list[:i]
                break
            i += 1
        (small_list, big_list) = self.order_lists(small_list, big_list)
        j = len(big_list) // 2
        while j > 0:
            if big_list[j] <= small_list[0]:
                head = big_list[:j]
                small_list = head + small_list
                big_list = big_list[j:]
                break
            j -= 1
        (small_list, big_list) = self.order_lists(small_list, big_list)
        return small_list, big_list

    def balance_lists(self, nums1, nums2):
        (small_list, big_list) = self.balance_large(nums1, nums2)
        while len(big_list) != len(small_list):
            small_list, big_list = self.switch_number_to_smaller_list(small_list, big_list)
        return self.order_lists(small_list, big_list)

    def prepare_lists(self, nums1, nums2):
        split_lists_are_even = ((len(nums1) + len(nums2)) / 2) % 2 == 0
        split_lists_unequal = (len(nums1) + len(nums2)) / 2 != (len(nums1) + len(nums2)) // 2
        merged_list_gt_four = (len(nums1) + len(nums2)) > 4
        while split_lists_are_even or split_lists_unequal and merged_list_gt_four:
            nums1, nums2 = self.remove_min(nums1, nums2)
            nums1, nums2 = self.remove_max(nums1, nums2)
            split_lists_are_even = ((len(nums1) + len(nums2)) / 2) % 2 == 0
            split_lists_unequal = (len(nums1) + len(nums2)) / 2 != (len(nums1) + len(nums2)) // 2
            merged_list_gt_four = (len(nums1) + len(nums2)) > 4

        (small_list, big_list) = self.order_lists(nums1, nums2)

        if not merged_list_gt_four:
            return small_list, big_list

        else:
            return self.balance_lists(small_list, big_list)

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

        if len(nums1) + len(nums2) < 5:
            return self.find_median(self.merge(nums1, nums2))

        if self.find_median(nums1) == self.find_median(nums2):
            return self.find_median(nums1)

        total_len_is_even = (len(nums1) + len(nums2)) % 2 == 0
        nums1_is_even = len(nums1) % 2 == 0
        nums2_is_even = len(nums2) % 2 == 0

        if nums1_is_even or nums2_is_even or len(nums1) != len(nums2):
            nums1, nums2 = self.prepare_lists(nums1, nums2)

        # Here, nums1 and nums2 should both be odd and have equal lengths.

        while len(nums1) > 2 and len(nums2) > 2:
            nums1_median = self.find_median(nums1)
            median_index = len(nums1) // 2
            nums2_median = self.find_median(nums2)
            if nums1_median == nums2_median:
                return nums1_median
            if nums1_median < nums2_median:
                nums1 = nums1[median_index:]
                nums2 = nums2[:median_index + 1]
            if nums1_median > nums2_median:
                nums1 = nums1[:median_index + 1]
                nums2 = nums2[median_index:]
        reduced_len_is_even = (len(nums1) + len(nums2)) % 2 == 0

        if not total_len_is_even == reduced_len_is_even:
            (nums1, nums2) = self.remove_min(nums1, nums2)
        merged = self.merge(nums1, nums2)
        return self.find_median(merged)
