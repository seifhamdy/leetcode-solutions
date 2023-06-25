class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for i in nums:
            if i in x:
                return True
            else:
                x.add(i)

# Runtime: 514 ms (beats 99.68%)
# Memory: 30.0 MB (beats 68.78%)
