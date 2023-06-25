class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True

# Runtime: 49 ms (beats 96.36%)
# Memory: 16.8 MB (beats 90.98%)
