from collections import defaultdict
class Solution:
    def dfs(self, adj_list, visit, node, parent):
        if node in visit:
            return False

        visit.add(node)

        for nei in adj_list[node]:
            if nei == parent:
                continue
            if not self.dfs(adj_list, visit, nei, node):
                return False
        
        return True

    def isValidTree(self, n, edges):
        if not n or len(edges) != n - 1:
            return False
        visit = set()
        adj_list = defaultdict(list)

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        return self.dfs(adj_list, visit, 0, -1) and n == len(visit)

s = Solution()

print(s.isValidTree(5, [[0,1],[0,2],[0,3],[1,4]]))
print(s.isValidTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))
