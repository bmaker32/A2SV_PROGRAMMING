# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self,nums):
        if len(nums) == 0:
            return None
        k = len(nums)//2
        head = TreeNode(nums[k])
        
        head.left = self.insert(nums[:k])
        head.right = self.insert(nums[k+1:])
        
        return head
        
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.insert(nums)
        
        
        