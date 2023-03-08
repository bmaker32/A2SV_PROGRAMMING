# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root1,root2):
        ans = []
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1 and not root2:
            return False
        if root1.val != root2.val:
            return False
        
        left = self.helper(root1.left,root2.right)
        right = self.helper(root2.left,root1.right)
        
        return left and right 
        
        
        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = self.helper(root.left,root.right)
        return left
    
        