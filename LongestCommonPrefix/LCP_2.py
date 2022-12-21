from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs[1:]:
            index = 0
            for prefix_c, string_c in zip(prefix, string):
                if prefix_c == string_c:
                    index += 1
                else:
                    break
            prefix = prefix[:index]
            if index == 0:
                return ""

        return prefix


def test_1():
    sol = Solution()
    example_1 = ["flower", "flow", "flight"]
    prefix_1 = "fl"
    ans_1 = sol.longestCommonPrefix(example_1)
    assert (ans_1 == prefix_1)


def test_2():
    sol = Solution()
    ex_2 = ["dog", "racecar", "car"]
    prefix = ""
    ans = sol.longestCommonPrefix(ex_2)
    assert (ans == prefix)

def test_3():
    sol = Solution()
    ex = ["ab", "a"]
    prefix = "a"
    ans = sol.longestCommonPrefix(ex)
    assert (ans == prefix)

def test_4():
    sol = Solution()
    ex = ["cir","car"]
    prefix = "c"
    ans = sol.longestCommonPrefix(ex)
    assert (ans == prefix)

def test_5():
    sol = Solution()
    ex = ["flower","flower","flower","flower"]
    prefix = "flower"
    ans = sol.longestCommonPrefix(ex)
    assert (ans == prefix)


test_1()
test_2()
test_3()
test_4()
test_5()
