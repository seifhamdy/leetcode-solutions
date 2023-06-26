class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        k = 1
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i += 1
                k += 1

        return k

# Runtime: 100 ms (beats 64.67%)
# Memory: 18.1 MB (beats 18.89%)
