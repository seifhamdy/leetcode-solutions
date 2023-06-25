class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}

        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        frequency_list = [(freq, num) for num, freq in frequency_map.items()]

        frequency_list.sort(key=lambda x: x[0], reverse=True)

        result = [num for freq, num in frequency_list[:k]]

        return result

# Rename: 106 ms (beats 93.44%)
# Memory: 21.3 MB (beats 29.24%)
