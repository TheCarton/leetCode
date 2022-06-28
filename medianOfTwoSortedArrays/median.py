"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))
"""


class Solution(object):
    def merge(self, nums1, nums2) -> list:
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
            return float((nums[middle_index] + nums[middle_index - 1]) / 2)
        else:
            return float(nums[middle_index])

    def remove_min_of_both(self, nums1, nums2) -> tuple[list, list]:
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

    def remove_max_of_both(self, nums1, nums2) -> tuple[list, list]:
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

    def switch_number_to_smaller_list(self, small_list, big_list) -> tuple[list, list]:
        if len(small_list) == 0:
            small_list.append(big_list.pop())
        elif big_list[0] <= small_list[0]:
            small_list.insert(0, big_list.pop(0))
        elif big_list[-1] >= small_list[-1]:
            small_list.append(big_list.pop())
        else:
            for i, n in enumerate(small_list):
                if big_list[0] <= n:
                    small_list.insert(i, big_list.pop(0))
                    break
        return small_list, big_list

    def order_lists(self, nums1, nums2) -> tuple[list, list]:
        if len(nums1) >= len(nums2):
            (small_list, big_list) = nums2, nums1
        else:
            (small_list, big_list) = nums1, nums2
        return small_list, big_list

    def insert_list(self, insert_list, receive_list) -> list:
        if insert_list[0] >= receive_list[-1]:
            receive_list = receive_list + insert_list
        elif insert_list[-1] <= receive_list[0]:
            receive_list = insert_list + receive_list
        else:
            receive_list = self.merge(insert_list, receive_list)
        return receive_list

    def balance_large(self, nums1, nums2) -> tuple[list, list]:
        (small_list, big_list) = self.order_lists(nums1, nums2)
        if len(small_list) == 0:
            small_list = big_list[:len(big_list) // 2]
            big_list = big_list[len(big_list) // 2:]
            return self.order_lists(small_list, big_list)

        len_diff = len(big_list) - len(small_list)
        if len_diff <= 1:
            return small_list, big_list

        big_middle = big_list[len(big_list) // 2]
        small_middle = small_list[len(small_list) // 2]
        delta_len = len_diff // 2
        if big_middle >= small_middle:
            delta = big_list[len(big_list) - delta_len:]
            big_list = big_list[:len(big_list) - delta_len]
        else:
            delta = big_list[:delta_len]
            big_list = big_list[delta_len:]
        small_list = self.insert_list(delta, small_list)
        return self.order_lists(small_list, big_list)

    def balance_lists(self, nums1, nums2) -> tuple[list, list]:
        small_list, big_list = self.order_lists(nums1, nums2)
        while len(big_list) - len(small_list) > 1:
            small_list, big_list = self.switch_number_to_smaller_list(small_list, big_list)
        return self.order_lists(small_list, big_list)

    def get_middle_value(self, nums) -> tuple[int, float]:
        middle_index = len(nums) // 2
        if len(nums) % 2 == 0:
            middle_index -= 1
        return middle_index, float(nums[middle_index])

    def reduce(self, small, large, left_rems, right_rems) -> tuple[list, list, int, int]:
        small_i, _ = self.get_middle_value(small)
        large_i, _ = self.get_middle_value(large)

        new_large = large[:large_i + 2]
        new_right_rems = right_rems - (len(large) - len(new_large))
        if new_right_rems >= 0:
            large = new_large
            right_rems = new_right_rems

        new_small = small[small_i:]
        new_left_rems = left_rems - (len(small) - len(new_small))
        if new_left_rems >= 0:
            small = new_small
            left_rems = new_left_rems

        return small, large, left_rems, right_rems

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) < 2 and len(nums2) < 2:
            merged = self.merge(nums1, nums2)
            return self.find_median(merged)

        nums1, nums2 = self.balance_large(nums1, nums2)
        nums1, nums2 = self.balance_lists(nums1, nums2)

        total_len_is_even = (len(nums1) + len(nums2)) % 2 == 0
        if total_len_is_even:
            left_rems = right_rems = (len(nums1) + len(nums2) - 2) / 2
        else:
            left_rems = right_rems = (len(nums1) + len(nums2) - 3) / 2

        while left_rems > 1 or right_rems > 1:
            _, nums1_middle = self.get_middle_value(nums1)
            _, nums2_middle = self.get_middle_value(nums2)
            if nums1_middle < nums2_middle:
                small = nums1
                large = nums2
            else:
                small = nums2
                large = nums1
            nums1, nums2, left_rems, right_rems = self.reduce(small, large, left_rems, right_rems)
            if left_rems > right_rems:
                self.remove_min_of_both(nums1, nums2)
                left_rems -= 1
            if right_rems > left_rems:
                self.remove_max_of_both(nums1, nums2)
                right_rems -= 1
            nums1, nums2 = self.balance_lists(nums1, nums2)

        if left_rems > 0:
            nums1, nums2 = self.remove_min_of_both(nums1, nums2)
        if right_rems > 0:
            nums1, nums2 = self.remove_max_of_both(nums1, nums2)

        merged = self.merge(nums1, nums2)
        return self.find_median(merged)
