class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if len(num) == 1:
            if int(num) == target:
                return [num]
            return []
        
        def get_nums(x):
            ar = []
            nu = ""
            for i in range(len(num)):
                nu += num[i]
                if (x & (1 <<i)):
                    ar.append(nu)
                    if len(nu) > 1 and nu[0] == '0':
                        return ar, 0
                    nu = ""
            ar.append(nu)
            if len(nu) > 1 and nu[0] == '0':
                return ar, 0
            return ar, 1
        
        mp_chr = ['-', '+','*']
        def generate_exps(ar, num):
            ans = ar[0]
            for j in range(1, len(ar)):
                ans += mp_chr[num % 3]
                ans += ar[j]
                num //= 3
            return ans
        
        def do_eval(ex):
            nu = 0
            ans = []
            for x in ex:
                if x in ('-', '+', '*'):
                    if len(ans) >= 2 and ans[-1] == '*':
                        val = ans[-2] * nu
                        ans.pop(); ans.pop()
                        ans.append(val)
                    else:
                        ans.append(nu)
                    ans.append(x)
                    nu = 0
                else:
                    nu = nu * 10 + int(x)

            if len(ans) >= 2 and ans[-1] == '*':
                val = ans[-2] * nu
                ans.pop(); ans.pop()
                ans.append(val)
            else:
                ans.append(nu)

            res = ans[0]
            for j in range(2, len(ans), 2):
                if ans[j - 1] == '-':
                    res -= ans[j]
                else:
                    res += ans[j]
            return res

                
        def get_exps(ar):
            le = len(ar)
            exps = []
            for j in range(pow(3, le - 1)):
                ex = generate_exps(ar, j)
                if do_eval(ex) == target:
                    exps.append(ex)
            return exps
            
        ans = []
        length = len(num)
        for i in range(pow(2, length - 1)):
            keda, valid = get_nums(i)
            if not valid:
                continue
            ans += get_exps(keda)

        return ans
        