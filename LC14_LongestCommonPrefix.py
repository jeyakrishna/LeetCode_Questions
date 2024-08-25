class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common = ""

        current = strs[0]
        for i in range(len(current)):
            for string in strs[1:]:
                if i > len(string) - 1  or current[i] != string[i]:
                    return common

            common += current[i]
        
        return common


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))