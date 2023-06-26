class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            char = strs[0][i]
            if any(s[i] != char for s in strs):
                return strs[0][:i]

        return strs[0][:min_len]

# Runtime: 55 ms (beats 30.95%)
# Memory: 16.2 MB (beats 95.77%)
