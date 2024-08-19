from typing import Optional

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        stack = []
        # print(stack)
        for i in prices:
            # print(f"Current Value of i = {i}")
            if stack and i < stack[-1]:
                stack.pop()
                stack.append(i)
            elif stack and i >= stack[-1]:
                profit = max(profit, i - stack[-1])
                # stack.pop()
            else:
                stack.append(i)
        return profit

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))