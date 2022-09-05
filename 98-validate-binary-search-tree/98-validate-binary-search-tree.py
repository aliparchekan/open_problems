# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validity(self, root, left, right):
        if root == None:
            return True
        if root.val >= right or root.val <= left:
            return False
        return self.validity(root.left, left, root.val) and self.validity(root.right, root.val, right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validity(root, float(-inf), float(inf))
        
        