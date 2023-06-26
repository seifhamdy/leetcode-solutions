class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# Runtime: 84 ms (beats 30.30%)
# Memory: 16.3 MB (beats 77%)
