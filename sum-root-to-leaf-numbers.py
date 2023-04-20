# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, acc_sum=0):
            nonlocal total
            if node.left is None and node.right is None:
                total += acc_sum*10 + node.val
            else:
                for leaf in ('left', 'right'):
                    if node.__dict__[leaf] is not None:
                        dfs(node.__dict__[leaf], acc_sum*10 + node.val)
        dfs(root)  
        return total