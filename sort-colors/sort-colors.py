class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        for i in range(3):
            for j in range(len(nums)):
                if nums[j] == i:
                    nums[start], nums[j] = nums[j], nums[start]
                    start += 1
                
        return nums