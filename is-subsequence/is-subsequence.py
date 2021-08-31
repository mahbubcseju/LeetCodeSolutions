class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        for i in range(len(s)):
            while ptr < len(t) and t[ptr] != s[i]:
                ptr = ptr + 1
            if ptr >= len(t) or t[ptr] != s[i]:
                return False
            ptr = ptr + 1
        return True
        