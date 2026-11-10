# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p # force p < q
        
        def bfs(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            if p.val > root.val and q.val >= root.val:
                return bfs(root.right, p, q)
            elif p.val <= root.val and q.val < root.val:
                return bfs(root.left, p, q)
            else:
                return root

        return bfs(root, p, q)