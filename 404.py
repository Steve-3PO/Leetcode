# Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        # recursive function
        def dfs(node):
            
            # return if no node
            if node is None:
                return 0
            
            # incase we need to add
            add = 0
            
            # if there is a left node and it has no children, add value
            if node.left and (node.left.left == None and node.left.right == None):
                add += node.left.val
            
            # return all node children and sum
            return add + dfs(node.left) + dfs(node.right)
        
        return dfs(root)