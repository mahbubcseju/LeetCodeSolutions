# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi, res = 1, n, n
        while lo <=hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res
