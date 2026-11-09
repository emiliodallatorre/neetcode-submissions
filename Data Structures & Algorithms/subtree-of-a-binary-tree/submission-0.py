# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        def dfs_compare(root: Optional[TreeNode], comparison: Optional[TreeNode]) -> bool:
            if not root or not comparison:
                return False

            equality: bool = root.val == comparison.val

            if not equality:
                return False

            if root.left or comparison.left:
                equality = equality and dfs_compare(root.left, comparison.left)
            if root.right or comparison.right:
                equality = equality and dfs_compare(root.right, comparison.right)

            return equality

        def dfs(root: Optional[TreeNode]) -> bool:
            if not root:
                return False

            if root.val == subRoot.val:
                if dfs_compare(root, subRoot):
                    return True
            
            left: bool = False
            right: bool = False

            if root.left:
                left = left or dfs(root.left)
            
            if root.right:
                right = right or dfs(root.right)

            return left or right

        return dfs(root)
                    