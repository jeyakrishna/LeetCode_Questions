class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) == 1:
            return t
        
        char_count = {}
        for i in range(len(s)):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
        
        for i in range(len(t)):
            char_count[t[i]] = char_count.get(t[i], 0) - 1

        for k, v in char_count.items():
            if v == -1:
                return k

s = Solution()
print(s.findTheDifference("abcd", "abcde"))
print(s.findTheDifference("", "y"))