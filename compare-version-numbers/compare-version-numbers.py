class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        print(v1, v2)
        mi = min(len(v1), len(v2))
        for i in range(mi):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        
        for j in range(mi, len(v1)):
            if v1[j] > 0:
                return 1
        for j in range(mi, len(v2)):
            if v2[j] > 0:
                return -1
        return 0
