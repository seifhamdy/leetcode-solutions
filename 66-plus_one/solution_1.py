class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10

        if carry:
            digits.insert(0, carry)

        return digits

# Runtime: 54 ms (beats 22.83%)
# Memory: 16.3 MB (beats 26.41%)
