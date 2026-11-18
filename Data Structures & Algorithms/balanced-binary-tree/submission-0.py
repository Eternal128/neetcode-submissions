# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        if not root:
            return True
        
        def height(node) -> int:
            if not node:
                return 0
            
            left, right = height(node.left), height(node.right) #left and right heights

            if abs(left - right) > 1:
                self.balanced = False
            
            return 1 + max(left, right) # return the max height at that node recursively
        
        height(root)
        return self.balanced

