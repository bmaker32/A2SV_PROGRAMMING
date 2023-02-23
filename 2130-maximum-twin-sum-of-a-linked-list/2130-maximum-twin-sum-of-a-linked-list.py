# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dum = left = right = head
        count = 0
        temp = ListNode()
        maxi = 0
        temp2 = ListNode()
        
        while right:
            temp = left
            right = right.next.next 
            left = left.next
            count += 1
            
        while left:
            con = left.next
            left.next = temp
            temp = left
            temp2 = left
            left = con
        
        
        left = temp2        
        right = head
        print(left.val,left.next.val)
        for i in range(count):
            if left and right:
                maxi = max(maxi,(left.val+right.val))
                print("maxi:",left.val," + ",right.val,"= ", maxi)
                left = left.next
                right = right.next
        
        return maxi 
        