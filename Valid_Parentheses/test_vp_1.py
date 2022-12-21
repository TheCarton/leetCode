from VP_1 import Solution


def test_ex1():
    sol = Solution()
    assert sol.isValid("()")

def test_ex2():
    sol = Solution()
    assert sol.isValid("()[]{}")


def test_ex3():
    sol = Solution()
    assert not sol.isValid("(]")


def test_incorrect_order():
    sol = Solution()
    assert sol.isValid("([])")


def test_one_char():
    sol = Solution()
    assert not sol.isValid("(")


def test_all_left():
    sol = Solution()
    assert not sol.isValid("((")
