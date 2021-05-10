class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        num_of_points = len(points)
        result = min(2, num_of_points)  
        for i in range(num_of_points):
            for j in range(i + 1, num_of_points):
                cnt = 0
                for k in range(j + 1):
                    if (((points[k][1] - points[i][1]) * (points[k][0] - points[j][0])) 
                        == ((points[k][1] - points[j][1]) * (points[k][0] - points[i][0]))):
                        cnt += 1
                result = max(cnt, result)
        return result