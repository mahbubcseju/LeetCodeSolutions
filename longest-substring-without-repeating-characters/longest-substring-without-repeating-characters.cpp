class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int ar[257];
        memset(ar,0,sizeof ar);
        int st=0;
        int res=0;
        for(int i=0;i<s.size();i++)
        {
            int x=s[i];
            ar[x]++;
            
            while(ar[x]>1&&st<i)
            {
                ar[s[st++]]--;
               // st++;
            }
            res=max(i-st+1,res);
        }
        return res;
    }
};
