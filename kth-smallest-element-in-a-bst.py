class Solution:
        def __init__(self):
            self.countList = []
        def kthSmallest(self, root, k) -> int:
            ans = self.countList
            self.helper(root)
            print(self.countList)
            return ans[k-1]
        def helper(self, node):
            if not node:
                return
            self.helper(node.left)
            self.countList.append(node.val)
            self.helper(node.right)