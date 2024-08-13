from typing import Optional
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]

        def find(x):
            x = par[x]
            while x != par[x]:
                x = par[x]
            
            return x
        
        def union(x1, x2):
            px1, px2 = find(x1), find(x2)

            if px1 == px2:
                return False

            if rank[px1] == rank[px2]:
                par[px2] = px1
                rank[px1] += px2
            else:
                par[px2] = px1
                rank[px2] += px1

            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

s = Solution()
print(s.findRedundantConnection([[1,2],[1,3],[2,3]]))
print(s.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))