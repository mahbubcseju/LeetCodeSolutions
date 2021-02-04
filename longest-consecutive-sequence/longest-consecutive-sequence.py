class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums = sorted(nums)
        res, koto = 0, 0 
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1] + 1:
                koto = 1
            else:
                koto += 1
            res = max(res, koto)
        return res
                
        