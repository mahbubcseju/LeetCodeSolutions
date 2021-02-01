# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        le = len(nums) // 2
        
        current = TreeNode(nums[le])
        current.left = self.sortedArrayToBST(nums[:le])
        current.right = self.sortedArrayToBST(nums[le + 1:])
        return current