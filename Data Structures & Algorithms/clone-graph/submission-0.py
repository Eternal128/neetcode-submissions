"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: # if the graph is empty
            return None
        
        cloned_map = {} # hash map

        # dfs
        def dfs(curr):
            # return the clone if we already visited the node
            if curr in cloned_map:
                return cloned_map[curr]
            
            copy = Node(curr.val)
            cloned_map[curr] = copy

            # recursively clone all neighbors and add them
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)





        

# i will create my hash map to store the visited nodes so that it doesnt loop infinitely

# im gnna store the value of the nodes in the new created copy of the node and then recursively go through its neighborus


#
# normal case -> clone every node and neigbor is copied one time.
# empty graph -> return None
# single node -> return the node itself
# keep track of visited node


# i visit each node, check if i have already copied it, create a copy if not, and then loop through its neighbors 




