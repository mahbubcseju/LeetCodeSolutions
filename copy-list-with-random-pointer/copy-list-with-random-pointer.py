"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        dict = {}
        copy_head, res_head = None, None
        ptr_head = head
        
        while ptr_head:
            if not copy_head:
                copy_head = Node(ptr_head.val)
                res_head = copy_head
            else:
                copy_head.next = Node(ptr_head.val)
                copy_head = copy_head.next
            dict[ptr_head] = copy_head
            ptr_head = ptr_head.next
        
        ptr_head, copy_head = head, res_head
        while ptr_head:
            if ptr_head.random:
                copy_head.random = dict[ptr_head.random]
            copy_head, ptr_head = copy_head.next, ptr_head.next
        
        return res_head