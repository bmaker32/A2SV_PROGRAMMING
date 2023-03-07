# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trial(self,root):
        if not root:
            return 0
        left = 1 + self.trial(root.left)
        right = 1 + self.trial(root.right)
        return (max(left,right))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.trial(root)
        