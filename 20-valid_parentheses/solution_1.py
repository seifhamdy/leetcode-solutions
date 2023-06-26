class Solution:
    def isValid(self, s: str) -> bool:
        stack = ''
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in bracket_map.values():
                stack += char
            elif char in bracket_map.keys():
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack = stack[:-1]

        return not stack

# Runtime: 51 ms (beats 35.46%)
# Memory: 16.3 MB (beats 50.38%)
