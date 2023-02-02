# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = current=dummy = ListNode(0,head)
        
        for i in range(n):
            current = current.next
            
        while current.next:
            current = current.next
            prev = prev.next
        prev.next = prev.next.next
        
        return dummy.next
            
            
            