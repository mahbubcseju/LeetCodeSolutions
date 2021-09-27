# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dic = [{} for j in range(3)]
        def howMuch(root, pre=2, dic=None):
            if not root:
                return 0
            if root in dic[pre]:
                return dic[pre][root]
            if pre == 1:
                ret = howMuch(root.left, 0, dic) + howMuch(root.right, 0, dic)
            else:
                ret = max(
                    root.val + howMuch(root.left, 1, dic) + howMuch(root.right, 1, dic),
                    howMuch(root.left, 0, dic) + howMuch(root.right, 0, dic)
                )
            dic[pre][root] = ret
            return dic[pre][root]
        return howMuch(root, 2, dic)
                