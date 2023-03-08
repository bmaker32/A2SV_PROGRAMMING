# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxval = 0
        
    def traverse(self,root,pre):
        count = 0
        if not root:
            return 0
        
        
        
        
        left = self.traverse(root.left,root)
        right = self.traverse(root.right,root)
        
        self.maxval = max(self.maxval, left+right)
        
        if not pre or root.val == pre.val:
            return (max(left,right)+1) 
        else:
            return 0
        
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.traverse(root,None)
        return self.maxval
        
    
    

        