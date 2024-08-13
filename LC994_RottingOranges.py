from typing import Optional
from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh, time = 0, 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    x = r + dr
                    y = c + dc

                    if x < 0 or y < 0 or x == rows or y == cols or grid[x][y] != 1:
                        continue
                    
                    grid[x][y] = 2
                    queue.append((x, y))
                    fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1
       
s = Solution()
print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
