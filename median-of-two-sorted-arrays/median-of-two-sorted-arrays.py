import bisect
​
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def find(nth):
​
            len1, len2 = len(nums1), len(nums2)
            lo, hi = min(nums1[0] if nums1 else 0, nums2[0] if nums2 else 0), (nums1[len1-1]  if nums1 else 0) + (nums2[len2-1] if nums2 else 0)
            result = 0
            
            while lo <= hi:
                mid = (lo + hi) // 2
                
                pos = bisect.bisect_left(nums1, mid) 
                pos += bisect.bisect_left(nums2, mid) 
                if pos >= nth:
                    hi = mid - 1
                else:
                    result = mid
                    lo = mid + 1
​
            return result
                
        totalSize = len(nums1) + len(nums2)
        return find(totalSize/2 + 1) if totalSize % 2 else float(find(totalSize/2) + find(totalSize/2 + 1))/2 
        
