class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for j in nums:
            if nums.count(j) == 1:
                return j