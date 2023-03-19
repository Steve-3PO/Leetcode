# Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        # to create a copy we will use a hashmap that makes old nodes to new nodes
        old_new = {}

        # doing recursively around the circular path
        def dfs(node):

            # if we have seen the node we can just grab its copy
            if node in old_new:
                return old_new[node]

            # otherwise we make a copy of the node and assign within the hashmap
            copy = Node(node.val)
            old_new[node] = copy

            # going through all the neighbours of a given node, make copys and append to current neighbours variable
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            # we want to return the first copy as its the first node
            return copy
        
        return dfs(node) if node else None

            