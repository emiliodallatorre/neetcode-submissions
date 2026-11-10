# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        dq = deque([root])
        rightmost_nodes: list[int] = []

        while dq:
            level_size: int = len(dq)

            for i in range(level_size):
                node: TreeNode = dq.popleft()
                
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                
                if i == level_size - 1:
                    rightmost_nodes.append(node.val)

        return rightmost_nodes