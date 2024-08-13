from typing import Optional
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    visit.add((r, c))
        dist = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            for s in range(len(queue)):
                row, col = queue.popleft()
                rooms[row][col] = dist
                for dx, dy in directions:
                    x = row + dx
                    y = col + dy

                    if x < 0 or x >= rows or y < 0 or y >= rows or rooms[x][y] == -1 or (x, y) in visit:
                        continue
                        
                    visit.add((x, y))
                    queue.append((x, y))
                
            dist += 1
        
        return rooms




s = Solution()
print(s.wallsAndGates([[2147483647, -1, 0, 2147483647],
                 [2147483647, 2147483647, 2147483647, -1],
                 [2147483647, -1, 2147483647, -1],
                 [0, -1, 2147483647, 2147483647]]))