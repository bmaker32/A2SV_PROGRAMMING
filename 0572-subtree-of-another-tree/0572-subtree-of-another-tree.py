# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root1,root2):
        if not root1 and not root2:
            return True
        if not root1 and  root2:
            return False
        if not root2 and root1:
            return False
        if root2.val != root1.val:
            return False
        else:
            left = self.helper(root1.left,root2.left)
            right = self.helper(root1.right,root2.right)
            return left and right 
            
        
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.helper(root,subroot) or self.helper(root.left,subroot) or self.helper(root.right,subroot):
            return True
        
        return self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)
        
            
            
            
            
        