class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}':'{' }
        stack = []

        for paren in s:
            if paren in mapping:
                if stack and stack [-1] == mapping[paren]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(paren)
        return True if not stack else False