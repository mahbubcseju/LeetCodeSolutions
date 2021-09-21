class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ar = list(s)
        ss = s
        s = '#' + '@'.join(ar) + '$'
        n = len(s)
        
        mirrors = [1] * n
        center, left, right = 0, 0, 0
        result = 0
        for i in range(n):
            if i > right:
                center, left, right = i, i, i
                while left > 0 and right < n - 1 and s[left - 1] == s[right + 1]:
                        mirrors[i] += 1
                        left, right = left - 1, right + 1
            else:
                c_left = 2 * center - i
                mr = mirrors[c_left]
                kot = i + mr - 1
                if kot < right:
                    mirrors[i] = mr
                else:
                    center, left = i, 2 * i - right
                    mirrors[i] = right - i + 1
                    while left > 0 and s[left - 1] == s[right + 1]:
                        mirrors[i] += 1
                        left, right = left - 1, right + 1
            if left == 1:
                result = max(result, right // 2 + 1)

        return ss[result:][::-1] + ss
            
