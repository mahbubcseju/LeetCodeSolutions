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
        from queue import deque
        q = deque()
    
        q.appendleft((root, 0))
        print(q[0])
        while len(q):
            node, lev = q.popleft()
            if not node:
                continue
            if not len(q) or q[0][1] != lev:
                node.next = None
            else:
                node.next = q[0][0]
                
            q.append((node.left, lev + 1))
            q.append((node.right, lev + 1))
            
        return root