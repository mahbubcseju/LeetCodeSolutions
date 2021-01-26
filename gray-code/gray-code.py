class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        result = [0,1]
        for i in range(1,n):
            le = len(result)
            for j in range(le-1,-1, -1):
                print(j)
                result.append((1<<i)+result[j])
        return result

        