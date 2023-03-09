# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root1,root2):
        if not root1 and root2:
            return root2              
        if not root2 and root1:
            return root1 
        if not root1 and not root2:
            return None
        
        
        
        root1.val = root1.val + root2.val
        root1.right = self.helper(root1.right,root2.right)
        root1.left = self.helper(root1.left,root2.left)
        
        return root1
            
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper(root1,root2)

