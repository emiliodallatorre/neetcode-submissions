# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev: ListNode = None

        while head:
            if not rev:
                rev = ListNode(head.val)
            else:
                new_rev = ListNode(head.val)
                new_rev.next = rev
                rev = new_rev

            head = head.next
                    
        return rev