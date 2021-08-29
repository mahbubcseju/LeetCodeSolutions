# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def chk(ptr):
            if not ptr:
                return head, 0
            k, val = chk(ptr.next)
            if k.val != ptr.val:
                val = 1
            return k.next, val
        
        return chk(head)[1] == 0
                