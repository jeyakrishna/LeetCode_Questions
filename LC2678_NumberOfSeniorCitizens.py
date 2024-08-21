class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                count += 1
        
        return count
    
s = Solution()
print(s.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))
print(s.countSeniors(["1313579440F2036","2921522980M5644"]))