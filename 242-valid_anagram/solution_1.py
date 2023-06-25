class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            l = []
            for i in s:
                l.append(i)
            for j in t:
                if j in l:
                    l.remove(j)
            if len(l) == 0:
                return True

# Runtime: 1370 ms (beats 5.2%)
# Memory: 17.4 MB (beats 10.3%)
