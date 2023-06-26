class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys():
                if not stack or brackets[char] != stack.pop():
                    return False
            else:
                return False
        return not stack

# Runtime: 54 ms (beats 17.27%)
# Memory: 16.2 MB (beats 90.7%)
