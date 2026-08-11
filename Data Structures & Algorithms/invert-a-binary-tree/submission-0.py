# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue: list[TreeNode] = []
        if root:
            queue.append(root)

        while queue:
            for tree in queue:
                if tree.left or tree.right:
                    tree.left, tree.right = tree.right, tree.left

                    if tree.left:
                        queue.append(tree.left)
                    if tree.right:
                        queue.append(tree.right)

                queue.remove(tree)

        return root