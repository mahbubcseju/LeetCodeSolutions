class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        for i in range(32):
            if (n & (1<< i)) > 0:
                counter += 1
        return counter