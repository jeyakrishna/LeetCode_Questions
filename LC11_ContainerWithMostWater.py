from typing import Optional

class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater = 0
        l, r = 0, len(height) - 1

        while l < r:
            maxWater = max(maxWater, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))