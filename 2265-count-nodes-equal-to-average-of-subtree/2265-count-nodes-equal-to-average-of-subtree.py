# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def helper(self,root):
        summ = [0,0]
        left = [0,0]
        right = [0,0]
        if not root.right and not root.left:
            summ[0] = root.val
            summ[1] = 1
            self.ans += 1
            return summ
        
        if root.left:
            left = self.helper(root.left)
            
        if root.right:
            right = self.helper(root.right) 
            
        summ[0] = (left[0] + right[0] + root.val)
        summ[1] = (left[1] + right[1] + 1)
        
        if summ[1] != 0 and  summ[0]//summ[1] == root.val:
            self.ans += 1

        return summ
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        self.helper(root)
        return self.ans
        