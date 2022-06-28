import median
import random
import statistics


def test_merge():
    sol = median.Solution()
    a = [1, 2]
    b = [3]
    assert sol.merge(a, b) == [1, 2, 3]

    assert sol.merge([], []) == []

    assert sol.merge(b, []) == b

    assert sol.merge([], a) == a


def test_merge_2():
    sol = median.Solution()
    assert sol.merge([3], [1, 2]) == [1, 2, 3]


def test_order_lists():
    sol = median.Solution()
    assert sol.order_lists([1, 2, 3], []) == ([], [1, 2, 3])


def test_insert_list_a_inside_b():
    sol = median.Solution()
    a = [4, 5, 6, 7]
    b = [1, 20, 30]
    expected = sorted(a + b)
    inserted = sol.insert_list(a, b)
    assert inserted == expected


def test_insert_list_a_inside_b_two():
    sol = median.Solution()
    a = [1, 4, 9, 11]
    b = [1, 2, 3]
    expected = sorted(a + b)
    inserted = sol.insert_list(a, b)
    assert inserted == expected


def test_insert_list_a_before_b():
    sol = median.Solution()
    a = [-31, 0]
    b = [1, 20, 30]
    expected = sorted(a + b)
    inserted = sol.insert_list(a, b)
    assert inserted == expected


def test_insert_list_a_after_b():
    sol = median.Solution()
    a = [31, 33]
    b = [1, 20, 30]
    expected = sorted(a + b)
    inserted = sol.insert_list(a, b)
    assert inserted == expected


def test_order_lists_random():
    sol = median.Solution()
    for i in range(10):
        a_length = random.randint(0, 50)
        b_length = random.randint(0, 50)
        million = 1000000

        a = random.sample(range(-million, million), a_length)
        a.sort()
        b = random.sample(range(-million, million), b_length)
        b.sort()
        (small_actual, big_actual) = sol.order_lists(a, b)
        assert len(small_actual) <= len(big_actual)


def test_balance_large_test():
    sol = median.Solution()
    a = [1, 2, 3]
    b = [1, 4, 9, 11, 25, 63, 78, 100, 123, 155, 196]
    expected_median = statistics.median(a + b)
    actual_a, actual_b = sol.balance_large(a, b)
    remaining_median = statistics.median(actual_a + actual_b)
    assert len(actual_a) + len(actual_b) == len(a) + len(b)
    assert len(actual_b) - len(actual_a) <= 1
    assert actual_a == sorted(actual_a)
    assert actual_b == sorted(actual_b)
    assert remaining_median == expected_median


def test_balance_large_test_big_median_lt():
    sol = median.Solution()
    a = [1, 256, 300]
    b = [1, 4, 9, 11, 25, 63, 78, 100, 123, 155, 196]
    expected_median = statistics.median(a + b)
    actual_a, actual_b = sol.balance_large(a, b)
    remaining_median = statistics.median(actual_a + actual_b)
    assert len(actual_a) + len(actual_b) == len(a) + len(b)
    assert len(actual_b) - len(actual_a) <= 1
    assert actual_a == sorted(actual_a)
    assert actual_b == sorted(actual_b)
    assert remaining_median == expected_median


def test_balance_large_random():
    sol = median.Solution()
    for i in range(1000):
        a_length = random.randint(4, 1000)
        b_length = random.randint(0, 1000)
        million = 1000000

        a = random.sample(range(-million, million), a_length)
        a.sort()
        b = random.sample(range(-million, million), b_length)
        b.sort()

        expected_median = statistics.median(a + b)
        actual_a, actual_b = sol.balance_large(a, b)
        remaining_median = statistics.median(actual_a + actual_b)
        still_sorted = actual_a == sorted(actual_a) and actual_b == sorted(actual_b)
        balanced = len(actual_b) - len(actual_a) <= 1
        correct_size = len(actual_a) + len(actual_b) == len(a) + len(b)
        succeed = (expected_median == remaining_median) and balanced and still_sorted and correct_size
        if not succeed:
            print(a, b)
            print(actual_a, actual_b)
            print("Expected median = {}".format(expected_median))
            print("Remaining median = {}".format(remaining_median))
            print(f"Correct total size = {len(a) + len(b)}")
            print(f"Actual total size = {len(actual_a) + len(actual_b)}")
            print(f"Size difference = {len(actual_b) - len(actual_a)}")
        assert remaining_median == expected_median
        assert len(actual_b) - len(actual_a) <= 1
        assert actual_a == sorted(actual_a)
        assert actual_b == sorted(actual_b)


def test_balance_large_random_smaller_ints():
    sol = median.Solution()
    for i in range(1000):
        a_length = random.randint(3, 10)
        b_length = random.randint(0, 10)
        million = 1000000

        a = random.sample(range(-10, 10), a_length)
        a.sort()
        b = random.sample(range(-10, 10), b_length)
        b.sort()

        expected_median = statistics.median(a + b)
        actual_a, actual_b = sol.balance_large(a, b)
        remaining_median = statistics.median(actual_a + actual_b)
        still_sorted = actual_a == sorted(actual_a) and actual_b == sorted(actual_b)
        balanced = len(actual_b) - len(actual_a) <= 1
        correct_size = len(actual_a) + len(actual_b) == len(a) + len(b)
        succeed = (expected_median == remaining_median) and balanced and still_sorted and correct_size
        if not succeed:
            print(a, b)
            print(actual_a, actual_b)
            print("Expected median = {}".format(expected_median))
            print("Remaining median = {}".format(remaining_median))
            print(f"Correct total size = {len(a) + len(b)}")
            print(f"Actual total size = {len(actual_a) + len(actual_b)}")
            print(f"Size difference = {len(actual_b) - len(actual_a)}")
        assert remaining_median == expected_median
        assert len(actual_b) - len(actual_a) <= 1
        assert actual_a == sorted(actual_a)
        assert actual_b == sorted(actual_b)


def test_balance_large_singleton():
    sol = median.Solution()
    a = [1]
    b = [-9, -5, -4, 2, 4, 5, 6, 7, 9]
    expected_median = statistics.median(a + b)
    actual_a, actual_b = sol.balance_large(a, b)
    remaining_median = statistics.median(actual_a + actual_b)
    assert remaining_median == expected_median
    assert len(actual_b) - len(actual_a) <= 1
    assert actual_a == sorted(actual_a)
    assert actual_b == sorted(actual_b)


def test_balance_large_from_random():
    sol = median.Solution()
    a = [-10, -4, -2, 3, 7, 9]
    b = [-8, -2]

    expected_median = statistics.median(a + b)
    actual_a, actual_b = sol.balance_large(a, b)
    remaining_median = statistics.median(actual_a + actual_b)
    assert remaining_median == expected_median
    assert len(actual_b) - len(actual_a) <= 1
    assert actual_a == sorted(actual_a)
    assert actual_b == sorted(actual_b)


def test_balance_large_small_clamps_large_one():
    sol = median.Solution()
    a = [-1000, 10, 5000]
    b = [-200, -50, 0, 1, 7, 65, 100, 120, 121, 122, 156]
    expected_median = statistics.median(a + b)
    actual_a, actual_b = sol.balance_large(a, b)
    remaining_median = statistics.median(actual_a + actual_b)
    assert remaining_median == expected_median
    assert len(actual_b) - len(actual_a) <= 1
    assert actual_a == sorted(actual_a)
    assert actual_b == sorted(actual_b)


def test_balance_large_small_clamps_large_two():
    sol = median.Solution()
    a = [-1000, 400, 5000]
    b = [-200, -50, 0, 1, 7, 65, 100, 120, 121, 122, 156]
    expected_median = statistics.median(a + b)
    actual_a, actual_b = sol.balance_large(a, b)
    remaining_median = statistics.median(actual_a + actual_b)
    assert remaining_median == expected_median
    assert len(actual_b) - len(actual_a) <= 1
    assert actual_a == sorted(actual_a)
    assert actual_b == sorted(actual_b)


def test_balance_lists():
    sol = median.Solution()
    a = [-1, 10, 50]
    b = [-200, -50, 0, 1, 7, 65, 100, 120, 121, 122, 156]
    expected_median = statistics.median(a + b)
    actual_a, actual_b = sol.balance_lists(a, b)
    remaining_median = statistics.median(actual_a + actual_b)
    assert remaining_median == expected_median
    assert len(actual_b) - len(actual_a) <= 1
    assert actual_a == sorted(actual_a)
    assert actual_b == sorted(actual_b)


def test_balance_random_smaller_ints():
    sol = median.Solution()
    for i in range(1000):
        a_length = random.randint(0, 10)
        b_length = random.randint(1, 10)
        million = 1000000

        a = random.sample(range(-10, 10), a_length)
        a.sort()
        b = random.sample(range(-10, 10), b_length)
        b.sort()

        expected_median = statistics.median(a + b)
        actual_a, actual_b = sol.balance_large(a, b)
        remaining_median = statistics.median(actual_a + actual_b)
        still_sorted = actual_a == sorted(actual_a) and actual_b == sorted(actual_b)
        balanced = len(actual_b) - len(actual_a) <= 1
        correct_size = len(actual_a) + len(actual_b) == len(a) + len(b)
        succeed = (expected_median == remaining_median) and balanced and still_sorted and correct_size
        if not succeed:
            print(a, b)
            print(actual_a, actual_b)
            print("Expected median = {}".format(expected_median))
            print("Remaining median = {}".format(remaining_median))
            print(f"Correct total size = {len(a) + len(b)}")
            print(f"Actual total size = {len(actual_a) + len(actual_b)}")
            print(f"Size difference = {len(actual_b) - len(actual_a)}")
        assert remaining_median == expected_median
        assert len(actual_b) - len(actual_a) <= 1
        assert actual_a == sorted(actual_a)
        assert actual_b == sorted(actual_b)


def test_prepare_lists():
    sol = median.Solution()
    a = [-1, 10, 50]
    b = [-200, -50, 0, 1, 7, 65, 100, 120, 121, 122, 156, 569, 603]
    actual_a, actual_b = sol.balance_large(a, b)
    actual_a, actual_b = sol.balance_lists(actual_a, actual_b)
    assert actual_a == sorted(actual_a)
    assert actual_b == sorted(actual_b)
    assert len(actual_a) == len(actual_b)


def test_prepare_lists_random():
    sol = median.Solution()
    for i in range(10):
        a_length = random.randint(0, 1000)
        b_length = random.randint(1, 1000)
        million = 1000000

        a = random.sample(range(-million, million), a_length)
        a.sort()
        b = random.sample(range(-million, million), b_length)
        b.sort()
        expected_median = statistics.median(a + b)

        actual_a, actual_b = sol.balance_large(a, b)
        actual_a, actual_b = sol.balance_lists(actual_a, actual_b)
        remaining_median = statistics.median(actual_a + actual_b)

        assert actual_a == sorted(actual_a)
        assert actual_b == sorted(actual_b)
        assert 1 >= len(actual_b) - len(actual_a)
        assert remaining_median == expected_median


def test_switch_number_small_lt_big():
    sol = median.Solution()
    small = [-5, 0, 1]
    big = [2, 5, 6, 10, 15]
    actual_a, actual_b = sol.switch_number_to_smaller_list(small, big)
    assert actual_a, actual_b == ([-5, 0, 1, 15], [2, 5, 6, 10])


def test_switch_number_small_gt_big():
    sol = median.Solution()
    small = [20, 30, 41]
    big = [2, 5, 6, 10, 15]
    actual_a, actual_b = sol.switch_number_to_smaller_list(small, big)
    assert actual_a, actual_b == ([2, 20, 30, 41], [5, 6, 10])


def test_switch_number_small_mid_big():
    sol = median.Solution()
    small = [6, 6.5, 7]
    big = [2, 5, 6, 10, 15]
    actual_a, actual_b = sol.switch_number_to_smaller_list(small, big)
    assert actual_a, actual_b == ([6, 6, 6.5, 7], [2, 5, 10, 15])


def test_remove_min():
    sol = median.Solution()
    (a, b) = [-1, 0], [-50, 1]
    sol.remove_min_of_both(a, b)
    assert b == [1]
    assert a == [-1, 0]
    sol.remove_min_of_both(a, b)
    assert b == [1]
    assert a == [0]

    sol.remove_min_of_both(a, b)
    assert b == [1]
    assert a == []


def test_remove_max():
    sol = median.Solution()
    (a, b) = [1, 100], [-68, 10]
    sol.remove_max_of_both(a, b)
    assert a == [1]
    assert b == [-68, 10]
    sol.remove_max_of_both(a, b)
    assert (a, b) == ([1], [-68])


def test_find_median_size_two():
    sol = median.Solution()
    a = [1, 2]
    expected_median = statistics.median(a)
    assert sol.find_median(a) == expected_median


####################################################### Integration Tests #######################################################

def test_two_singletons():
    sol = median.Solution()
    assert sol.findMedianSortedArrays([1], [2]) == 1.5


def test_one_missing():
    sol = median.Solution()
    assert sol.findMedianSortedArrays([1], []) == 1
    assert sol.findMedianSortedArrays([], [5]) == 5


def test_find_median_two_arrays_small():
    sol = median.Solution()
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5


def test_two_arrays_mixed():
    sol = median.Solution()
    a = [-1, 9, 10]
    b = [0, 1, 7]
    expected_median = statistics.median(a + b)
    sol_median = sol.findMedianSortedArrays(a, b)
    assert sol_median == expected_median


def test_two_arrays_mixed_2():
    sol = median.Solution()
    a = [7, 21, 500]
    b = [1, 5, 7]
    expected_median = statistics.median(a + b)
    sol_median = sol.findMedianSortedArrays(a, b)
    assert sol_median == expected_median


def test_two_odd_arrays():
    sol = median.Solution()
    a = [9, 10, 20]
    b = [1, 7, 100]
    expected_median = statistics.median(a + b)  # 9.5
    sol_median = sol.findMedianSortedArrays(a, b)
    assert sol_median == expected_median


def test_two_arrays_size_four():
    sol = median.Solution()
    a = [-1, 9, 10, 20]
    b = [0, 1, 7, 100]
    expected_median = statistics.median(a + b)  # 8.0
    sol_median = sol.findMedianSortedArrays(a, b)

    assert sol_median == expected_median


def test_two_arrays_size_four_ordered():
    sol = median.Solution()
    a = [0, 1, 2, 3]
    b = [4, 5, 6, 7]
    expected_median = statistics.median(a + b)  # 8.0
    sol_median = sol.findMedianSortedArrays(a, b)

    assert sol_median == expected_median


def test_two_arrays_mixed_larger():
    sol = median.Solution()
    a = [-1, 6, 7, 21, 500]
    b = [0, 0.5, 1, 5, 7]
    expected_median = statistics.median(a + b)
    sol_median = sol.findMedianSortedArrays(a, b)
    assert sol_median == expected_median


def test_one_singleton_one_large():
    sol = median.Solution()
    a = [-1]
    b = [-50, 0, 1, 7, 65, 100]
    # [-50, -1, 0, 1, 7, 65, 100]
    expected_median = statistics.median(a + b)
    sol_median = sol.findMedianSortedArrays(a, b)
    assert sol_median == expected_median


def test_very_unbalanced():
    sol = median.Solution()
    a = [-1, 10, 50]
    b = [-200, -50, 0, 1, 7, 65, 100, 120, 121, 122, 156, 569, 603]
    # Merged is [-200, -50, -1, 0, 1, 7, 10, 50, 65, 100, 120, 121, 122, 156, 569, 603]
    expected_median = statistics.median(a + b)
    # 57.5
    sol_median = sol.findMedianSortedArrays(a, b)
    assert sol_median == expected_median


def test_two_arrays_same():
    sol = median.Solution()
    a = [1, 2, 3]
    b = [1, 2, 3]
    expected_median = statistics.median(a + b)

    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_two_arrays_same_median():
    sol = median.Solution()
    a = [-100, 2, 302]
    b = [1, 2, 50]
    expected_median = statistics.median(a + b)

    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_two_arrays_one_bigger_different_intervals():
    sol = median.Solution()
    a = [0, 2, 4]
    b = [10, 20, 30]
    expected_median = statistics.median(a + b)
    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_merge():
    sol = median.Solution()
    a = [0, 2]
    b = [-1, 1]
    expected_merge = sorted(a + b)
    actual = sol.merge(a, b)
    assert actual == expected_merge


def test_from_random():
    sol = median.Solution()
    a = [-7, -4, -3, -1, 2, 3, 5, 6, 7, 8]
    b = [-8, -7, -2, 0]
    # [-8, -7, -7, -4, -3, -2, -1, 0, 2, 3, 5, 6, 7, 8]
    # [-4, -3, -2, -1, 0, 2, 3, 5] 1
    # [-2, -1, 0, 2, 3] 2 nums1 = [-2, 0, 3] nums2 = [-1, 2] xxxxxx
    # sent to merge: n1: [0, 3] n2: [-1, 2]
    expected_median = statistics.median(a + b)
    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_same_size():
    sol = median.Solution()
    a = [-2, 0, 3, 5, 6, 7]
    b = [-8, -7, -7, -4, -3, -1]
    expected_median = statistics.median(a + b)
    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_balance_fifteen():
    sol = median.Solution()
    a = [-20, 60, 61]
    b = [-1, 5, 36, 41, 42, 43, 100, 101, 120, 121, 130, 135]
    expected_median = statistics.median(a + b)
    a_bal, b_bal = sol.balance_lists(a, b)
    remaining_median = statistics.median(a_bal + b_bal)
    assert len(b_bal) - len(a_bal) == 1
    assert expected_median == remaining_median
    assert len(a + b) == len(a_bal + b_bal)
    assert sorted(a_bal) == a_bal
    assert sorted(b_bal) == b_bal


def test_size_fifteen():
    sol = median.Solution()
    a = [-2, 0, 3, 5, 5, 6, 7]
    b = [-8, -7, -7, -4, -3, -1, 1, 20]
    # merged = [-8, -7, -7, -4, -3, -2, -1, 0, 1, 3, 5, 5, 6, 7, 20]
    # after while: nums1 = [-2, 0, 3], nums2 = [1, 20]
    expected_median = statistics.median(a + b)
    # median = 0
    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_lists_size_seven():
    sol = median.Solution()
    a = [-2, 0, 3, 5, 6, 7, 8]
    b = [-8, -7, -7, -4, -3, -1, 2]
    # merged, sorted: [-8, -7, -7, -4, -3, -2, -1, 0, 2, 3, 5, 6, 7, 8]
    #                                           _____
    expected_median = statistics.median(a + b)  # = -0.5
    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_total_size_twelve():
    sol = median.Solution()
    a = [-9, -6, -1, 4, 6, 8]
    b = [-9, -7, -6, -3, -2, 4]
    # m = [-9, -9, -7, -6, -6, -3, -2, -1, 4, 4, 6, 8]
    #                          _______
    expected_median = statistics.median(a + b)  # = -2.5
    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_unbalanced_size_twelve():
    sol = median.Solution()
    a = [-7, -3, -2, 1, 2, 5, 6, 8, 9]
    b = [-9, -8, 7]
    # m = [-9, -8, -7, -3, -2, 1, 2, 5, 6, 7, 8, 9]
    #                          _____
    expected_median = statistics.median(a + b)  # = 1.5
    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_randoms_small():
    SAMPLE_SIZE = 100
    for i in range(SAMPLE_SIZE):
        sol = median.Solution()
        r1_size = random.randint(0, 10)
        list_of_randoms1 = random.sample(range(-10, 10), r1_size)

        r2_size = random.randint(1, 10)
        list_of_randoms2 = random.sample(range(-10, 10), r2_size)
        median_of_both = statistics.median(list_of_randoms1 + list_of_randoms2)

        list_of_randoms1.sort()
        list_of_randoms2.sort()

        sol_median = sol.findMedianSortedArrays(list_of_randoms1, list_of_randoms2)

        passed = sol_median == median_of_both

        if not passed:
            print("\n")
            print(list_of_randoms1)
            print(list_of_randoms2)
            print("Real median: {}".format(median_of_both))
            print("Found median: {}".format(sol_median))

        assert passed


def test_randoms_large():
    SAMPLE_SIZE = 100
    for i in range(SAMPLE_SIZE):
        sol = median.Solution()
        million = 1000000

        r1_size = random.randint(0, 1000)
        list_of_randoms1 = random.sample(range(-million, million), r1_size)

        r2_size = random.randint(1, 1000)
        list_of_randoms2 = random.sample(range(-million, million), r2_size)
        expected_median = statistics.median(list_of_randoms1 + list_of_randoms2)

        list_of_randoms1.sort()
        list_of_randoms2.sort()

        sol_median = sol.findMedianSortedArrays(list_of_randoms1, list_of_randoms2)

        assert expected_median == sol_median
