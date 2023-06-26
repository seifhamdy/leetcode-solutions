class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        end = len(s) - 1

        while end >= 0 and s[end] == ' ':
            end -= 1

        while end >= 0 and s[end] != ' ':
            length += 1
            end -= 1

        return length

# Runtime: 47 ms (beats 53.82%)
# Memory: 16.2 MB (beats 98.97%)
