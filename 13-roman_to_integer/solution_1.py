class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i in s:
            sum += values[i]
        return sum

# Runtime: 61 ms (beats 70.88%)
# Memory: 16.2 MB (beats 98.39%)
