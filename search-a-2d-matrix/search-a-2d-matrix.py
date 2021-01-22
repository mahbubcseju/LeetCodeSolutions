class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import bisect
        if not matrix:
            return False
        lo, hi = 0, len(matrix) - 1
        col = len(matrix[0])
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target <= matrix[mid][col-1]:
                ind = bisect.bisect(matrix[mid], target)
                print(mid, ind)
                return ind != -1 and matrix[mid][ind - 1] == target
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                lo = mid + 1
                
        return False
            