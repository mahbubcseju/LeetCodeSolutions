class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mi = min(nums)
        result = 0
        for m in nums:
            result += m - mi
        return result