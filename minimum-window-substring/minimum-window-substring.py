class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lenght = len(t)
        list = [0] * 256
        for ch in t:
            k = ord(ch) 
            list[k] += 1
            
        su = 0
        for j in list:
            if j:
                su += 1
        cnt = 0
        ans, x, y = len(s) + 1, 0, 0
        st, en = 0, 0
        
        list1 = [0] * 256
        
        while en < len(s):
            ch = ord(s[en])
            list1[ch] += 1
            if list1[ch] == list[ch]:
                cnt += 1
            en += 1  

            while st < len(s):
                c = ord(s[st]) 
                if list1[c] <= list[c]:
                    break;
                list1[c] -= 1
                st += 1
            
            print(cnt, su)
            
            if cnt == su and en-st < ans:
        
                ans = en-st
                x, y = st, en
        
        return s[x:y] if ans <= len(s) else ""