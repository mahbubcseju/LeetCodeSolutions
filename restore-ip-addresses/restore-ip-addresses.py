class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check_part(s):
            k = s.split('.')
            if len(k) > 4:
                return False
            for pe in k:
                if pe == '' or (len(pe) > 1 and pe[0] == '0'):
                    return False
                if int(pe) > 255:
                    return False
            return True
        def HM(s):
            return len(s.split('.')) == 4
        def Sex(ar, ind, ans, res):
            if ind == len(ar):
                if HM(ans) and check_part(ans):
                    res.append(ans)
                return
            if check_part(ans + ar[ind]):
                Sex(ar, ind + 1, ans + ar[ind], res)
            if check_part(ans + '.' + ar[ind]):
                Sex(ar, ind + 1, ans + '.' + ar[ind], res)
        res = []
        Sex(s, 0, "", res)
        return res
                    
            