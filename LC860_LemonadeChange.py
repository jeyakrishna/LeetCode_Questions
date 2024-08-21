class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fiveCount = 0
        tenCount = 0

        for bill in bills:
            if bill == 5:
                fiveCount += 1
            elif bill == 10:
                if fiveCount:
                    fiveCount -= 1
                    tenCount += 1
                else:
                    return False
            elif bill == 20:
                if tenCount >= 1 and fiveCount >= 1:
                    tenCount -= 1
                    fiveCount -= 1
                elif fiveCount >= 3:
                    fiveCount -= 3
                else:
                    return False
        return True

s = Solution()
print(s.lemonadeChange([5,5,5,10,20]))
print(s.lemonadeChange([5,5,10,10,20]))