# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dq = deque([root])

        result: list[list[int]] = []

        while dq:
            level_size: int = len(dq)
            result.append([])

            for _ in range(level_size):
                node: TreeNode = dq.popleft()
                result[-1].append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return result