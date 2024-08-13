from typing import Optional

class Solution:
    def trap(self, height: list[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        res = 0

        maxLeft[0] = height[0]
        maxRight[len(height) - 1] = height[len(height) - 1]

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])
        
        for i in range(1, len(height) - 1):
            res += (min(maxLeft[i], maxRight[i]) - height[i])

        return res

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))