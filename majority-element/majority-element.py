class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort(key=lambda x:  -x)
        
        cnt = 0
        for i, el in enumerate(nums):
            if i == 0 or nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt * 2 >= len(nums):
                return el