# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, node2parent, parent):
        if not node:
            return None
        
        node2parent[node.val] = parent
        self.dfs(node.left, node2parent, node)
        self.dfs(node.right, node2parent, node)
        

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        node2parent = {}
        
        self.dfs(root, node2parent, None)
        
        q = collections.deque([(target, 0)])
        visited = set([target.val])
        
        while q:
            cur_dist = q[0][1]
            
            if cur_dist == k:
                return [node.val for node, _ in q]
            
            node, _ = q.popleft()
            neigbs = [node.left, node.right, node2parent[node.val]]
            
            for neigb in neigbs:
                if neigb and neigb.val not in visited:
                    q.append((neigb, cur_dist + 1))
                    visited.add(neigb.val)
        
        return []