class Solution:
    def romanToInt(self, s: str) -> int:
        VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        for i in range(len(s)):
            if i < len(s) - 1 and VALUES[s[i]] < VALUES[s[i + 1]]:
                result -= VALUES[s[i]]
            else:
                result += VALUES[s[i]]

        return result

s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))