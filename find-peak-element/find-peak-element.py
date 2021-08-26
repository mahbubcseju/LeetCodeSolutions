class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        
        lo, hi = 0, length - 1
        while lo <= hi:
            if lo == hi:
                return lo
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
