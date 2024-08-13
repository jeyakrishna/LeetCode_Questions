class Solution:
    
    # Using Recursion 

    # def check(self, s, start, end):
    #     left = start
    #     right = end - 1
    #     while left < right:
    #         if s[left] == s[right]:
    #             left += 1
    #             right -= 1
    #         else:
    #             return False
        
    #     return True
    
    # def longestPalindrome(self, s):
        
    #     for length in range(len(s), 0, -1):
    #         for start in range(len(s) - length + 1):
    #             print(f"start = {start}, lenght = {length}, string = {s[start : start + length]}")
    #             if self.check(s, start, start + length):
    #                 return s[start: start + length]
        
    #     return ""


    def longestPalindrome(self, s):
        res = ""
        resLen = 0

        def expand(l, r, resLen, res):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l: r + 1]
                l -= 1
                r += 1
            return resLen, res
        
        for i in range(len(s)):
            l, r = i, i
            resLen, res = expand(l, r, resLen, res)
            
            l, r = i, i + 1
            resLen, res = expand(l, r, resLen, res)
        
        return res

s = Solution()
print(s.longestPalindrome('racecar'))
print(s.longestPalindrome('babad'))
print(s.longestPalindrome('cbbd'))
