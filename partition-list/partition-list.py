# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        while True:
            ptr = head
            checker = True
            while ptr:
                child = ptr.next
                if child and ptr.val >= x and child.val < x:
                    ptr.val, child.val = child.val, ptr.val
                    checker = False
                ptr = child
            if checker:
                break
        return head
        