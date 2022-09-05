# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
        
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = root
        minimum = min(p.val,q.val)
        maximum = max(p.val,q.val)
        while True:
            if minimum <= result.val and maximum >= result.val:
                return result
            if minimum < result.val and maximum < result.val:
                result = result.left
            else:
                result = result.right
            
        
        