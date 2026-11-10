# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes: int = 0

        def dfs(root: TreeNode, max_so_far: int) -> int:
            good_nodes: int = 0

            if root.val >= max_so_far:
                good_nodes += 1

            if root.left:
                good_nodes += dfs(root.left, max(max_so_far, root.val))
            
            if root.right:
                good_nodes += dfs(root.right, max(max_so_far, root.val))
            
            return good_nodes
        
        return dfs(root, root.val)