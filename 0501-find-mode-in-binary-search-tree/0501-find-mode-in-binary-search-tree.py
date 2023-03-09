# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root,dic):
        if not root:
            return None
        
        dic[root.val] += 1
          
        
        self.helper(root.left,dic)
        self.helper(root.right,dic)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        # trial = [1,1,2,2]
        # k = Counter(trial)
        # print("crowd:",max(k),k)
        
        self.helper(root,dic)
        ans = dict(Counter(dic))
        ans2 = []
        j = max(ans.values())
        for key in ans:
            if ans[key] == j:
                ans2.append(key)
            
        return ans2
        