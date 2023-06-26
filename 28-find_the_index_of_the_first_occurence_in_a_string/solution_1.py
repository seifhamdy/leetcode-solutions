class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        needle_length = len(needle)
        for i in range(len(haystack) - needle_length + 1):
            if haystack[i:i+needle_length] == needle:
                return i

        return -1

# Runtime: 40 ms (beats 87.78%)
# Memory: 16.3 MB (beats 28.89%)
