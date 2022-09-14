# Count Good Nodes in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # initialise a global count variable
        count = 0
        
        # define a function that has a root and largest value seen input
        def dfs(root, largest):
            
            # return if empty node
            if root is None:
                return 0
            
            # call a global variable
            nonlocal count
            
            # if the root value is larger than current seen, increment count
            if root.val >= largest:
                count += 1
            
            # run function on next children nodes if not none with updated max
            if root.left is not None:
                dfs(root.left, max(root.val, largest))
            if root.right is not None:
                dfs(root.right, max(root.val, largest))
         
        dfs(root, root.val)
        
        return count