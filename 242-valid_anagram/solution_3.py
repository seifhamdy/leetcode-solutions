class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        # Update the character count for string s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Check the character count for string t
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

            # Remove the character from the dictionary if count becomes zero
            if char_count[char] == 0:
                del char_count[char]

        return True

# Runtime: 66 ms (beats 63.35%)
# Memory: 16.8 MB (beats 90.98%)
