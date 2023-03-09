# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,root,p,q):
        if not root.left and not root.right:
            return root.val
        
        
        
        if root.val == p.val or root.val == q.val:
            return root
        if p.val > root.val and q.val < root.val:
            return root
        if p.val < root.val and q.val > root.val:
            return root 
        
        if p.val < root.val and q.val < root.val:
            return self.helper(root.left,p,q)
            
        if p.val > root.val and q.val > root.val:
            return self.helper(root.right,p,q)
        
        return None
            
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root,p,q)