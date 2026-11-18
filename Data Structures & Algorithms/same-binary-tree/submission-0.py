# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # if they're both empty then they match
            return True

        if not p or not q: # if one of them is empty then they don't match
            return False
        
        if p.val != q.val: # if the values aren't the same
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) #when the subtrees match