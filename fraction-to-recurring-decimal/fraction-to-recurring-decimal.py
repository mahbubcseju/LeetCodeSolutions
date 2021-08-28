class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        dict = {}
        flag = 0
        result = ""
        x, y = numerator, denominator
        
        if x == 0:
            return "0"
        
        minus = 0
        if  x < 0 and y < 0:
            x *= -1
            y *= -1
        elif x < 0 :
            minus = 1
            x *= -1
        elif y < 0:
            minus = 1
            y *= -1
        
        while x:
            k = x // y
            if not flag:
                if k:
                    result += str(k)
                    x %= y
                else:
                    flag = 1
                    if result == "":
                        result += "0."
                    else:
                        result += "."
            else:
                if x not in dict:
                    dict[x] = len(result)
                else:
                    result = list(result)
                    result[dict[x]:dict[x]] = '('
                    result = "".join(result)
                    result += ")"
                    break
                x *= 10
                while x // y == 0:
                    result += "0"
                    x *= 10
                result += str(x // y)
                x %= y
        
        return ("-" if minus else "") + result
                
                