class Solution:
    def level_order(self, root, height):
        if root:
            if len(self.levels) <= height:
                self.levels.append(0)
            if height > 1:
                if self.levels[height - 2] % 2 == 0:
                    self._sum += root.val                    

            self.levels[height] = root.val
            self.level_order(root.left, height + 1)
            self.level_order(root.right, height + 1)
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self._sum = 0
        self.levels = []
        self.level_order(root, 0)
        return self._sum