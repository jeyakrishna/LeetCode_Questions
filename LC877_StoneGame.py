class Solution:
    # TP With Outside Functions
    # def __init__(self):
    #     self.dp = {}

    # def dfs(self, l, r, aliceTurn, piles):
    #     if (l, r, aliceTurn) in self.dp:
    #         return self.dp[(l, r, aliceTurn)]
        
    #     if l >= r:
    #         return 0

    #     aliceScore, bobScore = 0, 0

    #     if aliceTurn:
    #         aliceScore = max(self.dfs(l, r - 1, not aliceTurn, piles) + piles[r], self.dfs(l + 1, r, not aliceTurn, piles) + piles[l])
    #     else: 
    #         bobScore = max(self.dfs(l, r - 1, not aliceTurn, piles) + piles[r], self.dfs(l + 1, r, not aliceTurn, piles) + piles[l])
        
    #     self.dp[(l, r, aliceTurn)] = aliceScore > bobScore

    #     return self.dp[(l, r, aliceTurn)]

    # def stoneGame(self, piles : list[int]) -> bool:
        
    #     return self.dfs(0, len(piles) - 1, True, piles)

    def stoneGame(self, piles : list[int]) -> bool:
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            left = piles[l] if (r - l) % 2 == 0 else 0
            right = piles[r] if (r - l) % 2 == 0 else 0

            dp[(l, r)] = max(dfs(l, r - 1) + right, dfs(l + 1, r) + left)
            return dp[(l, r)]

        return dfs(0, len(piles) - 1) > sum(piles) // 2

s = Solution()

print(s.stoneGame([5, 3, 4, 5]))
print(s.stoneGame([3, 7, 2, 3]))