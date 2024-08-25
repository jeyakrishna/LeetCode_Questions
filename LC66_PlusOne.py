class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            num = carry + digits[i]
            digits[i] = num % 10
            carry = num // 10

        if carry:
            digits.insert(0, carry)
        
        return digits

s = Solution()
print(s.plusOne([1, 2, 3]))
print(s.plusOne([4, 3, 2, 1]))
print(s.plusOne([9]))