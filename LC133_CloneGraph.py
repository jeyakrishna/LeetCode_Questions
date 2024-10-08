from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val, [])
        self.visited[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone_node

s = Solution()
print(s.cloneGraph([[2,4],[1,3],[2,4],[1,3]]))

        
