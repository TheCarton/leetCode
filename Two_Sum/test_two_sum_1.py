import two_sum_1

def test_ex1():
    sol = two_sum_1.Solution()
    ans = sol.twoSum([2, 7, 11, 15], 9)
    assert ans == [1, 0]