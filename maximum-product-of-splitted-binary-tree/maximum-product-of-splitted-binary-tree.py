# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def findTotalSum(curNode):
            if not curNode:
                return 0
            return curNode.val + findTotalSum(curNode.left) + findTotalSum(curNode.right)
        
        self.total_sum = findTotalSum(root)
        
        self.result = 0
        def findMaxProduct(curNode):
            if not curNode:
                return 0
            lol = curNode.val + findMaxProduct(curNode.left) + findMaxProduct(curNode.right)
            self.result = max(self.result, ((self.total_sum - lol) * lol))
            return lol
        
        findMaxProduct(root)
        return self.result % 1000000007