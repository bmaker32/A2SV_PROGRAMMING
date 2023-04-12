# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""
        def helper(node):
            nonlocal res
            if not node: return None
            
            res += str(node.val)
            if node.left or node.right:
                res += "("
                helper(node.left)
                res += ")"
            if node.right:
                res += "("
                helper(node.right)
                res += ")"
        helper(root)
        return res