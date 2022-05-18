import median
import random
import statistics


def test_find_median_singleton():
    sol = median.Solution()
    assert sol.find_median([1]) == 1


def test_find_median_odd():
    sol = median.Solution()
    assert sol.find_median([1, 2, 3]) == 2
    assert sol.find_median([1, 2, 3, 4, 5]) == 3


def test_find_median_even():
    sol = median.Solution()
    assert sol.find_median([1, 2]) == 1.5
    assert sol.find_median([1, 3]) == 2


def test_find_median_two_arrays_small():
    sol = median.Solution()
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5


def test_two_arrays_mixed():
    sol = median.Solution()
    a = [-1, 9, 10]
    b = [0, 1, 7]
    expected_median = statistics.median(a + b)
    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_two_arrays_one_bigger_different_intervals():
    sol = median.Solution()
    a = [0, 2, 4]
    b = [10, 20, 30]
    expected_median = statistics.median(a + b)
    assert sol.findMedianSortedArrays(a, b) == expected_median


def test_two_singletons():
    sol = median.Solution()
    assert sol.findMedianSortedArrays([1], [2]) == 1.5


def test_one_missing():
    sol = median.Solution()
    assert sol.findMedianSortedArrays([1], []) == 1
    assert sol.findMedianSortedArrays([], [5]) == 5


def test_randoms():
    sol = median.Solution()
    million = 1000000
    list_of_randoms1 = random.sample(range(-million, million), 50)
    list_of_randoms2 = random.sample(range(-million, million), 50)
    median_of_both = statistics.median(list_of_randoms1 + list_of_randoms2)

    list_of_randoms1.sort()
    list_of_randoms2.sort()

    assert sol.findMedianSortedArrays(list_of_randoms1, list_of_randoms2) == median_of_both
