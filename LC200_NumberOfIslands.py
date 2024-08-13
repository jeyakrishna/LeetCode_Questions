class Solution:
    def dfs(self, r, c, grid):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1':
            return
        
        grid[r][c] = '0'
        self.dfs(r + 1, c, grid)
        self.dfs(r - 1, c, grid)
        self.dfs(r, c + 1, grid)
        self.dfs(r, c - 1, grid)

    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    self.dfs(r, c, grid)
        
        return count

s = Solution()
print(s.numIslands([["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]))
print(s.numIslands([["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]))