class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)

        for i in range(n - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10

        if carry:
            return [carry] + digits

        return digits

# Runtime: 45 ms (beats 78.78%)
# Memory: 16.3 MB (beats 26.41%)
