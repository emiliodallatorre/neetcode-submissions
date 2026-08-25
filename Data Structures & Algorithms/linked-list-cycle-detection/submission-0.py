# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        already_seen: set = set()
        cyclic: bool = False

        while head and not cyclic:
            size_before: int = len(already_seen)
            already_seen.add(head)
            
            if len(already_seen) == size_before:
                cyclic = True

            head = head.next

        return cyclic