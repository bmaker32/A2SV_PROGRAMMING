# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,strin,ans):

        if not root.left and not root.right:
            ans.append(strin + str(root.val))
            return 
        if root.left:
            self.helper(root.left,strin + str(root.val) + "->",ans)
        if root.right:
            self.helper(root.right,strin + str(root.val) + "->",ans)
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        self.helper(root,"",ans)
        return ans
        
        