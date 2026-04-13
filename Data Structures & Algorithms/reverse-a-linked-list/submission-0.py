# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        curr = head
        curr2 = head.next
        head.next = None

        while curr2:
            temp = curr2.next
            curr2.next = curr
            curr = curr2
            curr2 = temp
        return curr
        