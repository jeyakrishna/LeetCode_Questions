class Solution:
    def countComponents(self, n, edges):
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != parent[res]:
                res = parent[res]
            
            return res

        def union(n1, n2):
            px, py = find(n1), find(n2)

            if px == py:
                return 0

            if rank[px] > rank[py]:
                parent[py] = px
                rank[px] += rank[py]
            else:
                parent[px] = py
                rank[py] += rank[px]
            
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res


