# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root:
            q = []
            q.append(root)
            while q:
                res = []
                for _ in range(len(q)):
                    temp = q[0]
                    q = q[1:]
                    res.append(temp.val)
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                result.append(res)
        return result
                    
            
            