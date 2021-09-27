class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import bisect
        left = bisect.bisect_left(nums, target)
        if left < len(nums) and nums[left] == target:
            return left
        else:
            return -1