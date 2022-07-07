# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverseTree(node, dict_):
            if not node:
                return
            if node.val not in dict_:
                dict_[node.val] = 1
            else:
                dict_[node.val] += 1
            traverseTree(node.left, dict_)
            traverseTree(node.right, dict_)
        
        dict_ = {}
        traverseTree(root, dict_)
        
        max_ = max(list(dict_.values()))
        
        return [ele for ele, values in dict_.items() if values == max_ ]