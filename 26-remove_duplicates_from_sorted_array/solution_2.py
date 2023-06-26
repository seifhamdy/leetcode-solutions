class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        k = 1
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                k += 1

        return k

# Runtime: 99 ms (beats 69.9%)
# Memory: 17.9 MB (beats 93.64%)
