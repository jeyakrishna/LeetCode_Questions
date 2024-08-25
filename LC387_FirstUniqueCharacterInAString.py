class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = [0] * 26

        for c in s:
            chars[ord(c) - 97] += 1
        
        for c in range(len(s)):
            if chars[ord(s[c]) - 97] == 1:
                return c
        
        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))