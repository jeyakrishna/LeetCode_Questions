class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if i + needle_len <= len(haystack) and haystack[i : i + needle_len] == needle:
                    return i
        
        return -1

s = Solution()
print(s.strStr("sadbutsad", "sad"))
print(s.strStr("leetcode", "leeto"))