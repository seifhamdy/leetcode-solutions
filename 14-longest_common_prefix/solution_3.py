class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()  # Sort the strings in lexicographic order

        shortest = strs[0]
        longest = strs[-1]

        min_len = min(len(shortest), len(longest))

        for i in range(min_len):
            if shortest[i] != longest[i]:
                return shortest[:i]

        return shortest[:min_len]

# Runtime: 36 ms (beats 98.48%)
# Memory: 16.5 MB (beats 28.18%)
