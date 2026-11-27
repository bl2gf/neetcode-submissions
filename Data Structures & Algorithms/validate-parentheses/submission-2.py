class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '(': ')',
            '{':'}',
            '[': ']'
        }
        for c in s:
            if c in brackets.keys():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c != brackets[stack.pop()]:
                    return False
        return len(stack) == 0