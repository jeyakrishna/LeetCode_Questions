from typing import Optional

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int):
        prices =[float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices[:]
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if p + prices[s] < tempPrices[d]:
                    tempPrices[d] = p + prices[s]
            
            prices = tempPrices
        
        return prices[dst]



s = Solution()
print(s.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))

print(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))

print(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0))
