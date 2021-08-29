class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        try:
            dict, dict_rev = {}, {}
            for i in range(len(s)):
                if s[i] not in dict and t[i] not in dict_rev:
                    dict[s[i]] = t[i]
                    dict_rev[t[i]] = s[i]
                elif dict[s[i]] != t[i] or dict_rev[t[i]] != s[i]:
                    return False
        except:
            return False

        return True
