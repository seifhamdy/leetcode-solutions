class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

# Runtime: 74 ms (beats 65.9%)
# Memory: 16.2 MB (beats 97.41%)
