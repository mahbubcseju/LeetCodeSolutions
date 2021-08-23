class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n, ma = len(nums), max(nums)
        size = int(sqrt(ma) + 1)
        buckets = [[] for i in range(size + 1)]
        
        for num in nums:
            buckets[num//size].append(num)
        
        for bucket in buckets:
            bucket.sort()
        
        result, last  = 0, -1
        for i in range(len(buckets)):
            for j in range(1, len(buckets[i])):
                result = max(result, buckets[i][j] - buckets[i][j - 1])
            if last > -1 and buckets[i]:
                result = max(result, buckets[i][0] - last)
            if buckets[i]:
                last = buckets[i][-1]
        
        return result