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


def test_two_arrays_size_four():
    sol = median_recur.Solution()
    a = [-1, 9, 10, 20]
    b = [0, 1, 7, 100]
    expected_median = statistics.median(a + b)
    sol_median = sol.findMedianSortedArrays(a, b)
    assert sol_median == expected_median


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


def test_randoms():
    sol = median_recur.Solution()
    million = 1000000
    list_of_randoms1 = random.sample(range(-million, million), 50)
    list_of_randoms2 = random.sample(range(-million, million), 50)
    median_of_both = statistics.median(list_of_randoms1 + list_of_randoms2)

    list_of_randoms1.sort()
    list_of_randoms2.sort()

    assert sol.findMedianSortedArrays(list_of_randoms1, list_of_randoms2) == median_of_both
