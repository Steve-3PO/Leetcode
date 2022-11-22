# Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        # define recursive function
        def search(root):
            
            # if node doesnt exist return 0, depth doesnt increase
            if not root:
                return 0
        
            # if both sides exist then take the minimum
            if root.left and root.right:
                return 1 + min(search(root.left), search(root.right))
            
            # or only take one side if it has 1 child node
            elif root.right:
                return 1 + search(root.right)
            else:
                return 1 + search(root.left)
            
        
        return search(root)