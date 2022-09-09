# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = deque()
        if root1==None:
            return root2
        if root2 == None:
            return root1
        stack.append((root1, root2))
        while stack:
            l, r = stack.popleft()
            if r == None:
                continue
            l.val += r.val
            if l.right == None:
                l.right = r.right
            else:
                stack.append((l.right, r.right))
            if l.left == None:
                l.left = r.left
            else:
                stack.append((l.left, r.left))
            
        return root1
                
            
        