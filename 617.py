# Merge Two Binary Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # check edge case that neither root exists
        if not root1 and not root2:
            return None
        
        # create 2 values otherwise 0 if null
        value1 = root1.val if root1 else 0
        value2 = root2.val if root2 else 0
        
        # create root passing total value as input
        root = TreeNode(value1 + value2)
        
        # assign the left child and right child recursively
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
    
        return root
            