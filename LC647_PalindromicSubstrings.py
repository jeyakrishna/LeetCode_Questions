from typing import Optional
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def check(l, r, count):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1

                l -= 1
                r += 1
            
            return count

        for i in range(len(s)):
            l, r = i, i
            count = check(l, r, count)

            l, r = i, i + 1
            count = check(l, r, count)
        
        return count

s = Solution()
print(s.countSubstrings('abc'))
print(s.countSubstrings('aaa'))