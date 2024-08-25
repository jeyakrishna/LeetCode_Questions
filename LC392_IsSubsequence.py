class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            if len(t) == 0:
                return True
            else:
                return False
        pos = 0

        for c in t:
            if s[pos] == c:
                pos += 1
                if pos == len(s):
                    return True
        
        return pos == len(s)

s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("axc", "ahbgdc"))