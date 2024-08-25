class Solution:
    def toHex(self, num: int) -> str:
        hexa  = "0123456789abcdef"
        ot = ""

        if num == 0:
            return "0"
        elif num < 0:
            num += 2 ** 32
        
        while num:
            ot = hexa[num % 16] + ot
            num = num // 16
        
        return ot

s = Solution()
print(s.toHex(26))
print(s.toHex(-1))