# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def get_order(root, res, lev):
            if not root:
                return
            if len(res) < lev + 1:
                res.append([root.val])
            else:
                res[lev].append(root.val)
            get_order(root.left, res, lev + 1)
            get_order(root.right, res, lev + 1)
        ans = []
        get_order(root, ans, 0)
        return ans[::-1]
            