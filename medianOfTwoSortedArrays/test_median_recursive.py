import median_recur
import random
import statistics


def test_merge():
    sol = median_recur.Solution()
    a = [1, 2]
    b = [3]
    assert sol.merge(a, b) == [1, 2, 3]

    assert sol.merge([], []) == []

    assert sol.merge(b, []) == b

    assert sol.merge([], a) == a


def test_merge_2():
    sol = median_recur.Solution()
    assert sol.merge([3], [1, 2]) == [1, 2, 3]


def test_find_median_singleton():
    sol = median_recur.Solution()
    assert sol.find_median([1]) == 1


def test_find_median_odd():
    sol = median_recur.Solution()
    assert sol.find_median([1, 2, 3]) == 2
    assert sol.find_median([1, 2, 3, 4, 5]) == 3


def test_find_median_even():
    sol = median_recur.Solution()
    assert sol.find_median([1, 2]) == 1.5
    assert sol.find_median([1, 3]) == 2


def test_remove_min():
    sol = median_recur.Solution()
    (a, b) = [-1, 0], [-50, 1]
    sol.remove_min(a, b)
    assert b == [1]
    assert a == [-1, 0]
    sol.remove_min(a, b)
    assert b == [1]
    assert a == [0]

    sol.remove_min(a, b)
    assert b == [1]
    assert a == []


def test_remove_max():
    sol = median_recur.Solution()
    (a, b) = [1, 100], [-68, 10]
    sol.remove_max(a, b)
    assert a == [1]
    assert b == [-68, 10]
    sol.remove_max(a, b)
    assert (a, b) == ([1], [-68])


def test_reduce_larger():
    sol = median_recur.Solution()
    (a, b) = sol.reduce_larger([1, 2, 10, 20, 50], [1, 2])
    assert a == [1, 2] and b == [1, 2]


def test_reduce_larger_mixed():
    sol = median_recur.Solution()
    (a, b) = sol.reduce_larger([10, 20, 50, 1000], [1, 2])
    assert a == [10, 20] and b == [1, 2]


def test_find_median_two_arrays_small():
    sol = median_recur.Solution()
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5


def test_two_arrays_mixed():
    sol = median_recur.Solution()
    a = [-1, 9, 10]
    b = [0, 1, 7]
    expected_median = statistics.median(a + b)
    sol_median = sol.findMedianSortedArrays(a, b)
    assert sol_median == expected_median


def test_two_arrays_mixed_2():
    sol = median_recur.Solution()
    a = [7, 21, 500]
    b = [1, 5, 7]
    expected_median = statistics.median(a + b)
    sol_median = sol.findMedianSortedArrays(a, b)
    assert sol_median == expected_median


def test_make_lists_odd():
    sol = median_recur.Solution()
    a = [-1, 9, 10, 20]
    b = [0, 1, 7, 100]
    a, b = sol.make_lists_odd(a, b)
    assert a, b == ([9, 10, 20], [1, 7, 100])


def test_two_odd_arrays():
    sol = median_recur.Solution()
    a = [9, 10, 20]
    b = [1, 7, 100]
    expected_median = statistics.median(a + b)  # 9.5
    sol_median = sol.findMedianSortedArrays(a, b)
    assert sol_median == expected_median


def test_two_arrays_size_four():
    sol = median_recur.Solution()
    a = [-1, 9, 10, 20]
    b = [0, 1, 7, 100]
    expected_median = statistics.median(a + b)  # 8.0
    sol_median = sol.findMedianSortedArrays(a, b)

    assert sol_median == expected_median


def test_two_arrays_mixed_larger():
    sol = median_recur.Solution()
    a = [-1, 6, 7, 21, 500]
    b = [0, 0.5, 1, 5, 7]
    expected_median = statistics.median(a + b)
    sol_median = sol.findMedianSortedArrays(a, b)
    assert sol_median == expected_median


def test_one_singleton_one_large():
    sol = median_recur.Solution()
    a = [-1]
    b = [-50, 0, 1, 7, 65, 100]
    expected_median = statistics.median(a + b)
    sol_median = sol.findMedianSortedArrays(a, b)
    assert sol_median == expected_median


def test_two_arrays_same():
    sol = median_recur.Solution()
    a = [1, 2, 3]
    b = [1, 2, 3]
    expected_median = statistics.median(a + b)

    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_two_arrays_same_median():
    sol = median_recur.Solution()
    a = [-100, 2, 302]
    b = [1, 2, 50]
    expected_median = statistics.median(a + b)

    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_two_arrays_one_bigger_different_intervals():
    sol = median_recur.Solution()
    a = [0, 2, 4]
    b = [10, 20, 30]
    expected_median = statistics.median(a + b)
    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_two_singletons():
    sol = median_recur.Solution()
    assert sol.findMedianSortedArrays([1], [2]) == 1.5


def test_one_missing():
    sol = median_recur.Solution()
    assert sol.findMedianSortedArrays([1], []) == 1
    assert sol.findMedianSortedArrays([], [5]) == 5


def test_from_random():
    sol = median_recur.Solution()
    a = [-10, -6, -4, -3, 0, 2, 4, 7, 8, 9]
    b = [-7, -5, -4, -2, -1, 1, 3, 6, 7, 8]
    expected_median = statistics.median(a + b)
    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_randoms():
    sol = median_recur.Solution()
    million = 1000000
    list_of_randoms1 = random.sample(range(-10, 10), 10)
    list_of_randoms2 = random.sample(range(-10, 10), 10)
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
