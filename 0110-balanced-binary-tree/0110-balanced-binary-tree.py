# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if not root:
            return [0,True]
        
        if self.helper(root.left)[1] and self.helper(root.right)[1]:
            left = self.helper(root.left)[0]
            right = self.helper(root.right)[0] 
        else:
            return [0,False]
        
        
        if abs(left-right) > 1:
            return [0,False]
        else:
        
            return [max(left,right)+1,True]
        
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        count = 0
        return self.helper(root)[1]
        
        
        