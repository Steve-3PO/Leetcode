# Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # initialise a variable to track the largest path seen
        res = [root.val]

        # define a search function
        def dfs(node):

            # if there is no node we want to return 0
            if not node:
                return 0

            # assign left/right for the left.right branch
            left = dfs(node.left)
            right = dfs(node.right)

            # if the branch is less than 0 we should choose note to take it 
            left = max(left, 0)
            right = max(right, 0)

            # check if it is the longest path seen so far through the root
            res[0] = max(res[0], left + right + node.val)
            
            # return the longer single path upwards
            return node.val + max(left, right)
        
        dfs(root)

        return res[0]

