# Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # intialise the max diameter we have seen
        res = 0
        
        # depth first search through the tree
        def dfs(root):
            
            if root is None:
                return 0
            
            # reach the bottom node first and calculate length upwards
            left = dfs(root.left)
            right = dfs(root.right)
            
            # tells python to look outside function for the result variable
            nonlocal res
            
            # checks if current node diameter is larger than the largest we have seen
            res = max(res, left + right)
            
            # return the height + 1, so that when we calculate diameter for the parent node we use height
            return 1 + max(left, right)
        
        dfs(root)
        
        return res