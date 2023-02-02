# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right == left: return head
        dummy =  ListNode(0,next=head)
        slow = dummy
        i = 1
        
        while i < left:
            slow = slow.next
            i+=1
        current = slow.next
        next_node = current.next
        while i < right:
            tmp = next_node.next
            next_node.next = current
            current = next_node
            next_node = tmp
            i+=1
        slow.next.next = next_node
        slow.next = current
        return dummy.next
        
            
                
            
            
            
            
            
            
#         [1,2,3,4,5]