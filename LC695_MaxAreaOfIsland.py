from typing import Optional

class Solution:
    def maxAreaOfLand(self, grid: list[list[int]]) -> int:
        maxLand = 0
        if not grid:
            return 0
        
        def dfs(r, c):
            
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0

            totalLand = 1
            grid[r][c] = 0

            totalLand += dfs(r - 1, c)
            totalLand += dfs(r + 1, c)
            totalLand += dfs(r, c - 1)
            totalLand += dfs(r, c + 1)

            return totalLand
        
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxLand = max(maxLand, dfs(r, c))
        
        return maxLand

s = Solution()
print(s.maxAreaOfLand([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
                 [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
                 [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))

print(s.maxAreaOfLand([[0,0,0,0,0,0,0,0]]))