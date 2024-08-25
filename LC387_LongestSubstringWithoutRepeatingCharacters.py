from typing import Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start two pointers at the left
        # keeping moving var right and keep on adding it to the set
        # stop moving right when the right is already in set. 
        # Keep moving left until the same var as right is removed
        l, r, longest, chars = 0, 0, 0, set()
        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                longest = max(longest, r - l + 1)
                r += 1
            else:
                chars.remove(s[l])
                l += 1
        
        return longest

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))