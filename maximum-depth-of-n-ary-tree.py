"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        def dfs(root,height,maxD):
            maxD=max(height,maxD)
            for child in root.children:
                #root has children then increment height
                maxD=dfs(child,height+1,maxD)#Take max depth
            return maxD
        
        return dfs(root,1,1)