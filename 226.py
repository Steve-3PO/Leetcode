# Invert Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            
            # if root doesnt exist, return
            if root is None:
                return
            
            # swap the root children around
            ph1 = root.left
            root.left = root.right
            root.right = ph1
            
            # dfs into both childrem
            dfs(root.left)
            dfs(root.right)
                
        dfs(root)
        
        return root