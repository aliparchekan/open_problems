"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        stack = []
        stack.append([root.left, root.right])
        flag = True
        while flag:
            elements = stack[0]
            stack = stack[1:]
            new_elements = []
            for i in range(len(elements) - 1):
                if elements[i] == None:
                    flag = False
                    continue
                elements[i].next = elements[i + 1]
                new_elements.append(elements[i].left)
                new_elements.append(elements[i].right)
            if len(elements) > 1 and elements[len(elements) - 1] != None:
                new_elements.append(elements[len(elements) - 1].left)
                new_elements.append(elements[len(elements) - 1].right)
            stack.append(new_elements)
        return root
            
            
                