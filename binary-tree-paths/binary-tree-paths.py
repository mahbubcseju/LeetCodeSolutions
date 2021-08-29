# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def recur(root1, par):
            if not root1:
                return []
            if not root1.left and not root1.right:
                return [par + str(root1.val)]
            x = recur(root1.left, "{}{}->".format(par, root1.val))
            y = recur(root1.right, "{}{}->".format(par, root1.val))
            return x + y
        return recur(root, "")