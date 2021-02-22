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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        def reallyConnect(root1, left):
            if not root1:
                return None
            
            right = left.next if left else None
            
            if left:
                left.next = root1
            
            newLeft, newRight = None, None
            if root1.left:
                newLeft = reallyConnect(root1.left, right)
                newRight = reallyConnect(root1.right, newLeft)
            else:
                newRight = reallyConnect(root1.right, right)
                
            if  newRight:
                root1.next = newRight
            elif newLeft:
                root1.next  = newLeft
            else:
                root1.next = right
            
            return root1
        
        reallyConnect(root, None)
        
        ptr = root
        while ptr.next:
            nex = ptr.next
            ptr.next = None
            ptr = nex
        return root