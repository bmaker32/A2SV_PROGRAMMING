# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nv = []
        cur = head
        while cur:
            nv.append(cur.val)
            cur = cur.next
        output = [0] * len(nv)
        stack = []
        for i, v in enumerate(nv):
            while stack and nv[stack[-1]] < v:
                output[stack.pop()] = v
            stack.append(i)
        return output