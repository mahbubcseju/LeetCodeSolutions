# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def check(head):
            last = head
            pre = None
            while last:
                if pre and pre.val > last.val:
                    return False, head, last
                pre = last
                if not  last.next:
                    break
                last = last.next
            return True, head, last

        def devide_and_conquer(head):
            if not head:
                return None, None
            if not head.next:
                return head, head
            
            is_sorted, head, leg = check(head)
            if is_sorted:
                return head, leg
                
            
            left, left_last = None, None
            right, right_last = None, None
            mid = head
            head = head.next
            mid.next = None
            
            while head:
                if head.val >= mid.val:
                    if not right:
                        right, right_last = head, head
                    else:
                        right_last.next = head
                        right_last = right_last.next
                else:
                    if not left:
                        left, left_last = head, head
                    else:
                        left_last.next = head
                        left_last = left_last.next
                head = head.next
 
            if left:
                left_last.next = None
                sorted_left_head, sorted_left_leg = devide_and_conquer(left)
                sorted_left_leg.next = mid
            else:
                sorted_left_head, sorted_left_leg = mid, mid
                
            if right:
                right_last.next = None
                sorted_right_head, sorted_right_leg = devide_and_conquer(right)
                mid.next = sorted_right_head
            else:
                sorted_right_leg = mid
                
            return sorted_left_head, sorted_right_leg
        
        return devide_and_conquer(head)[0]