class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        odd = False
        total = 0

        for i in s:
            counts[i] = counts.get(i, 0) + 1
        
        for k, v in counts.items():
            if v % 2 == 0:
                total += v
            else:
                odd = True
                total += (v - 1)
        
        return total + 1 if odd else total

s = Solution()
print(s.longestPalindrome("abccccdd"))
print(s.longestPalindrome("a"))