class Solution:
    def isPalindrome(self, s: str) -> bool:
        from functools import reduce
        
        s = reduce(lambda x, y: x + (s[y].lower() if s[y].isalnum() else ''), range(len(s)), '')

        return s == s[::-1]