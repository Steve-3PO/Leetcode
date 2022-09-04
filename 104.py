# Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # max depth variable to track
    maxdepth = 1
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # if no root exists return 0
        if root is None:
            return 0
        
        def dfs(self, depth, root):
            
            # check for a new max depth
            self.maxdepth = max(self.maxdepth, depth)
            
            # if node children exist, continue iteration with depth + 1
            if root.left is not None:
                dfs(self, depth + 1, root.left)
            if root.right is not None:
                dfs(self, depth + 1, root.right)
                
        dfs(self, 1, root)
        
        return self.maxdepth