# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p== None and q != None:
            return False
        elif p != None and q == None:
            return False
        elif p.val != q.val:
            return False
        lft = self.isSameTree(p.left,q.left)
        rgt = self.isSameTree(p.right,q.right)
        return lft and rgt
        