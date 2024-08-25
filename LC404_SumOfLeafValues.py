from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            
            total = 0
            if node.left:
                if node.left.left is None and node.left.right is None:
                    total += node.left.val
                total += dfs(node.left)
            
            if node.right:
                total += dfs(node.right)
            
            return total
            
        return dfs(root)

    
def createBinaryTree(arr, index = 0):
    if index < len(arr):
        if arr[index] is None:
            return None
        
        root = TreeNode(arr[index])
        root.left = createBinaryTree(arr, 2 * index + 1)
        root.right = createBinaryTree(arr, 2 * index + 2)
        return root
    return None


s = Solution()
root1 = createBinaryTree([3,9,20,None,None,15,7])
print(s.sumOfLeftLeaves(root1))

root2 = createBinaryTree([1])
print(s.sumOfLeftLeaves(root2))