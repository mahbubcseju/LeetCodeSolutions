# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        def get_length(cur):
            if not cur:
                return 0
            return 1 + get_length(cur.next)
        
        def find_kth(prev, cur, kth):
            if kth == 0:
                if prev:
                    prev.next = None
                right = cur.next
                cur.next = None
                return cur, right
            return find_kth(cur, cur.next, kth - 1)
        
        length = get_length(head)
        he, right = find_kth(None, head, length // 2)
        
        return TreeNode(he.val, self.sortedListToBST(head) if he !=head else None, self.sortedListToBST(right))
