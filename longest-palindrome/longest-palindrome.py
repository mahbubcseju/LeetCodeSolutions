class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        
        res, flag = 0, 0
        for item, cnt in dic.items():
            res += cnt // 2
            if cnt % 2:
                flag = 1
        res *= 2
        res += flag
        return res
            