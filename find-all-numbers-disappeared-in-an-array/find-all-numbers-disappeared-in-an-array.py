class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans, dic = [], {}
        
        for el in nums:
            dic[el] = 1

        for i in range(1, n + 1):
            if i not in dic:
                ans.append(i)
        return ans
