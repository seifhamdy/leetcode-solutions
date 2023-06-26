class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()

        if len(words) == 0:
            return 0

        last_word = words[-1]
        return len(last_word)

# Runtime: 49 ms (beats 36.53%)
# Memory: 16.4 MB (beats 18.55%)
