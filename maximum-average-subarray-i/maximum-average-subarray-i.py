class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        su = sum(nums[:k])
        result = su / k
        for k1 in range(k, len(nums)):
            su += nums[k1]
            su -= nums[k1 - k]
            result = max(result, su / k)
        return result