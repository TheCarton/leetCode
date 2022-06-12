import first_missing_positive
import random


def find_missing_positive_brute(nums):
    nums.sort()
    i = 1
    for i in range(1, nums[-1] + 2):
        if i not in nums:
            break
    return i


def test_brute():
    nums = [-13, 77, 22, 32, 0, 85, 25, 10, -12, 57, -97, -35, -67, 44, 68, 92, 45, 55, 28, 15]
    correct = 1
    assert find_missing_positive_brute(nums) == correct


def test_find_new_right_missing_one():
    sol = first_missing_positive.Solution()
    new = sol.find_new_missing(3, 1, 2)
    assert new == 3


def test_find_new_right_missing_two():
    sol = first_missing_positive.Solution()
    new = sol.find_new_missing(15, 1, 2)
    assert new == 15


def test_find_new_right_missing_three():
    sol = first_missing_positive.Solution()
    new = sol.find_new_missing(15, 3, 6)
    assert new == 4


def test_find_new_right_missing_four():
    sol = first_missing_positive.Solution()
    new = sol.find_new_missing(6, 3, 4)
    assert new == 6


def test_find_new_missing_zero():
    sol = first_missing_positive.Solution()
    new = sol.find_new_missing(2, 0, 1)
    assert new == 2


def test_find_new_missing_zero_again():
    sol = first_missing_positive.Solution()
    new = sol.find_new_missing(5, 0, 3)
    assert new == 1


################ Main tests ################

def test_example_one():
    sol = first_missing_positive.Solution()
    n = [1, 2, 0]
    assert sol.firstMissingPositive(n) == 3


def test_example_two():
    sol = first_missing_positive.Solution()
    n = [3, 4, -1, 1]
    assert sol.firstMissingPositive(n) == 2


def test_example_three():
    sol = first_missing_positive.Solution()
    n = [7, 8, 9, 11, 12]
    assert sol.firstMissingPositive(n) == 1


def test_one_at_the_end():
    sol = first_missing_positive.Solution()
    n = [2, 8, 9, 11, 1]
    assert sol.firstMissingPositive(n) == 3


def test_remember_two():
    sol = first_missing_positive.Solution()
    n = [2, 3, 9, 11, 1]
    assert sol.firstMissingPositive(n) == 4


def test_almost_ordered():
    sol = first_missing_positive.Solution()
    n = [2, 3, 4, 11, 1]
    assert sol.firstMissingPositive(n) == 5


def test_repeat_two():
    sol = first_missing_positive.Solution()
    n = [2, 3, 4, 2, 1]
    assert sol.firstMissingPositive(n) == 5


def test_repeat_three():
    sol = first_missing_positive.Solution()
    n = [2, 3, 4, 3, 1]
    assert sol.firstMissingPositive(n) == 5


def test_repeat_three_big_number_in_front():
    sol = first_missing_positive.Solution()
    n = [20, 3, 4, 3, 1]
    assert sol.firstMissingPositive(n) == 2


def test_random_spread():
    SAMPLE_SIZE = 10000
    for i in range(SAMPLE_SIZE):
        sol = first_missing_positive.Solution()
        size = 1000
        randoms = random.choices(range(-100, 100), k=size - 1)
        randoms.append(random.randint(1, 100))
        smallest_positive = find_missing_positive_brute(randoms)
        passed = sol.firstMissingPositive(randoms) == smallest_positive
        if not passed:
            print(randoms)
        assert sol.firstMissingPositive(randoms) == smallest_positive


def test_random_concentrated():
    SAMPLE_SIZE = 10000
    for i in range(SAMPLE_SIZE):
        sol = first_missing_positive.Solution()
        size = 20
        randoms = random.choices(range(1, 10), k=size)
        smallest_positive = find_missing_positive_brute(randoms)
        passed = sol.firstMissingPositive(randoms) == smallest_positive
        if not passed:
            print(randoms)
        assert sol.firstMissingPositive(randoms) == smallest_positive
