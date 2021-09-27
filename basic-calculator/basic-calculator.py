class Solution:
    def calculate(self, s: str) -> int:
        without_sp = ""
        for ch in s:
            if ch != ' ':
                without_sp += ch
        
        ops = ('-', '+')
        def opify(x):
            res = ''
            for j in x:
                if len(res) > 0 and res[-1] in ops and j in ops:
                    if res[-1] != j:
                        res = res[:-1] + '-'
                    else:
                        res = res[:-1] + '+'
                else:
                    res += j
            if res[0].isdigit():
                res = '+' + res
            return res
        
        stack = []
        for j in without_sp:
            if j == ')':
                val = ''
                while stack[-1] != '(':
                    val += stack[-1][::-1]
                    stack.pop()
                stack.pop()
                res = self.calculate(''.join(val[::-1]))
                stack.append(str(res))
            else:
                stack.append(j)
        
        final = opify(''.join(stack))
        return eval(final)