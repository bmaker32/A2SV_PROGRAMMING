class Solution:
    def __init__(self):
        self.ans = 0
    
    def dfs(self, root: Optional[TreeNode], targetSum: int, sm: int) -> None:
        if root is None:
            return
        if sm == targetSum:
            self.ans += 1
        if root.left:
            self.dfs(root.left, targetSum, sm + root.left.val)
        if root.right:
            self.dfs(root.right, targetSum, sm + root.right.val)
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.dfs(root, targetSum, root.val)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.ans