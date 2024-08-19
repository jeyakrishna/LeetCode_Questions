# At each stage, we can double and copy it or add the existing len to the current len
# i.e., copied len = 1 and current length = 2
# Opt 1 ->  current length = 2 * 2 = 4 and update copied len to 4 (2 operations)
# Opt 2 -> append copied len to current length (1  operation)

# Edge Cases
# If curr length > 1000, return 1000

# Case 1 - Recursion / Back Tracking
# from typing import Optional

# class Solution:
#     def __init__(self):
#         self.n = 0

#     def minStepsHelper(self, currentLength, pasteLength):
#         if currentLength == self.n:
#             return 0
        
#         if currentLength > self.n:
#             return 1000

#         opt1 = 2 + self.minStepsHelper(currentLength * 2, currentLength)
#         opt2 = 1 + self.minStepsHelper(currentLength + pasteLength, pasteLength)

#         return min(opt1, opt2)

    
#     def minSteps(self, n: int) -> int:
#         if n == 1:
#             return 0
        
#         self.n = n
#         return 1 + self.minStepsHelper(1, 1)

# Case 2 - Top Down DP
from typing import Optional

class Solution:
    def __init__(self):
        self.n = 0
        # self.memo = []

    def minStepsHelper(self, currentLength, pasteLength):
        if currentLength == self.n:
            return 0
        
        if currentLength > self.n:
            return 1000
        
        if self.memo[currentLength][pasteLength] != 0:
            return self.memo[currentLength][pasteLength]
        else:
            opt1 = 2 + self.minStepsHelper(currentLength * 2, currentLength)
            opt2 = 1 + self.minStepsHelper(currentLength + pasteLength, pasteLength)
            self.memo[currentLength][pasteLength] = min(opt1, opt2)

        return self.memo[currentLength][pasteLength]

    
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        self.n = n
        self.memo = [[0] * (n // 2 + 1) for _ in range(n + 1)]
        return 1 + self.minStepsHelper(1, 1)

s = Solution()
print(s.minSteps(3))
print(s.minSteps(1))
print(s.minSteps(20))