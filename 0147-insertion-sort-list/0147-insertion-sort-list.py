# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
            
        dummy = ListNode(val=-5000,next=head)
        lastsorted=head
        cur=head.next
        
        while cur:
            if lastsorted.val <= cur.val:
                lastsorted=lastsorted.next
                cur=cur.next
            else:
                prev=dummy
                while prev.next.val <= cur.val:
                    prev=prev.next
                lastsorted.next = cur.next
                cur.next = prev.next
                prev.next=cur
                cur = lastsorted.next
                
        return dummy.next
        