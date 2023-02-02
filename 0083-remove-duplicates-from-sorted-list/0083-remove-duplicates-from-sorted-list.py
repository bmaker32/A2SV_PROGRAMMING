# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = dummy=ListNode(0,head)
        slow =slow.next
        fast = fast.next
        while fast:
            if slow.val != fast.val:
                slow.next = fast
                slow = slow.next
            else:
                if fast.next is None and slow.val == fast.val:
                    slow.next = None
            fast = fast.next
        return dummy.next