class Solution:
    def matchParens(self, leftParen, rightParen) -> bool:
        if leftParen == '(':
            return rightParen == ')'
        elif leftParen == '[':
            return rightParen == ']'
        else:
            return rightParen == '}'

    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2:
            return False

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif stack:
                left_char = stack.pop()
                if not self.matchParens(left_char, char):
                    return False
            else:
                return False

        return len(stack) == 0