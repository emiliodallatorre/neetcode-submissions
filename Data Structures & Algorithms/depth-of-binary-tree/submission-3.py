# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack: list[TreeNode] = []
        if root:
            stack.append(root)

        max_depth: int = len(stack)

        while stack:
            deepest_node: TreeNode = stack[-1]

            if deepest_node.left:
                stack.append(deepest_node.left)
            elif deepest_node.right:
                stack.append(deepest_node.right)
            else:
                stack.remove(deepest_node)
                
                if stack:
                    if stack[-1].left == deepest_node:
                        stack[-1].left = None
                    elif stack[-1].right == deepest_node:
                        stack[-1].right = None
            
            max_depth = max(max_depth, len(stack))

        return max_depth
            