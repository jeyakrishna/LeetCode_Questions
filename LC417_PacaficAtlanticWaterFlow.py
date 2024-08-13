from collections import deque
from typing import Optional
class Solution:
    def pacificAtlantic(self, heights):
        p_queue = deque()
        p_seen = set()

        a_queue = deque()
        a_seen = set()

        m, n = len(heights), len(heights[0])

        for j in range(n):
            p_queue.append((0, j))
            p_seen.add((0, j))
        
        for i in range(1, m):
            p_queue.append((i, 0))
            p_seen.add((i, 0))
        
        for i in range(0, m):
            a_queue.append((i, n - 1))
            a_seen.add((i, n - 1))
        
        for j in range(0, n - 1):
            a_queue.append((m - 1, j))
            a_seen.add((m - 1, j))

        def get_coords(queue, visited):
            while queue:
                i, j = queue.popleft()
                for i_off, j_off in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < m and 0 <= c < n and (r, c) not in visited and heights[r][c] >= heights[i][j]:
                        visited.add((r, c))
                        queue.append((r, c))
        
        get_coords(p_queue, p_seen)
        get_coords(a_queue, a_seen)

        return list(p_seen.intersection(a_seen))

s = Solution()

# print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(s.pacificAtlantic([[1]]))