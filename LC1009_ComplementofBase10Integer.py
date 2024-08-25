class Solution:
    def bitwiseComplement(self, n: int) -> int:
        new = []
        if n == 0:
            return 1
        
        while n:
            new.append(n % 2)
            n = n // 2
        for i in range(len(new)):
            if new[i] == 0:
                new[i] = 1
            else:
                new[i] = 0
        
        total = 0
        for i in range(len(new)):
            total += (new[i] * 2 ** i)
        
        return total

s = Solution()
print(s.bitwiseComplement(5))
print(s.bitwiseComplement(7))
print(s.bitwiseComplement(10))