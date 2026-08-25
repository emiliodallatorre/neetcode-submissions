# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result: ListNode = None
        pointer: ListNode = None

        while list1 or list2:
            value: int = None

            if list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    value = list1.val
                    list1 = list1.next
                else:
                    value = list2.val
                    list2 = list2.next
            else:
                if list1 is None:
                    list1 = list2
                    list2 = None
                
                value = list1.val
                list1 = list1.next

            if result is None:
                result = ListNode(value)
                pointer = result
            else:
                pointer.next = ListNode(value)
                pointer = pointer.next
        
        return result
                