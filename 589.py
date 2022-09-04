# N-ary Tree Preorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        # need an empty list to append
        result = []
        
        # define a depth first search function passing in root
        def dfs(root):
            
            # if root is none then we can just return
            if root is None:
                return
        
            # otherwise we append the value of the root
            result.append(root.val)
            
            # for each node in the tree, go down through each child and recall
            # the function
            for node in root.children:
                dfs(node)
             
        dfs(root)
        return(result)