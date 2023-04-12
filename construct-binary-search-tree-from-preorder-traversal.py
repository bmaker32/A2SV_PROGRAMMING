# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def __init__(self):
        self.index = 0

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder,-sys.maxsize,sys.maxsize)
    
    def build(self,a,l,h):
        if(self.index >= len(a)):
            return None
        
        if(l <= a[self.index] <= h):
            index = self.index
            self.index += 1

            root = TreeNode(a[index])
            root.left = self.build(a,l,a[index])
            root.right = self.build(a,a[index],h)

            return root
        else:
            return None