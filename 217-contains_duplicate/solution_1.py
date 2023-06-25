class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = {}
        for i in nums:
            if i in x:
                if x[i] == 1:
                    return True
                    break
            else:
                x[i] = 1
        return False

# Runtime: 564 ms (beats 30.23%)
# Memory: 33.6 MB (beats 11.5%)
