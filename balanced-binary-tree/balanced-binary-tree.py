# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, rot):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def koto_dept(root):
            if root == None:
                return True, 0
            left_res, left = koto_dept(root.left)
            right_res, right = koto_dept(root.right)
            if not left_res or not right_res or abs(left - right) > 1:
                return False, 1 + max(left, right)
            else:
                return True, 1 + max(left, right)
        return koto_dept(rot)[0]