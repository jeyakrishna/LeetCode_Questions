from typing import Optional
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times : list[list[int]], n: int, k:int) -> int:
        edges = defaultdict(list)
        visit = set()

        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        t = 0

        while minHeap:
            t1, u1 = heapq.heappop(minHeap)
            if u1 in visit:
                continue
            visit.add(u1)
            t = max(t, t1)

            for u2, t2 in edges[u1]:
                if u2 not in visit:
                    heapq.heappush(minHeap, (t1 + t2, u2))
        
        return t if len(visit) == n else -1


        


s = Solution()
print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
print(s.networkDelayTime([[1,2,1]], 2, 1))
print(s.networkDelayTime([[1,2,1]], 2, 2))
