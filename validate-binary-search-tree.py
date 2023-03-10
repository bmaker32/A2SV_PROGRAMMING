# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.check = -float('inf')
        
    def helper(self,root):
        if not root:
            return True
        if not ( self.helper(root.left) and self.check < root.val):
            return False
        self.check = root.val

        return self.helper(root.right)

    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.helper(root)