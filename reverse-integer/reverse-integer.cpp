class Solution {
​
    public:
    int reverse(int x) {
        long long res=x;
        
        bool fl=0;
        if(res<0){
            res*=-1;
            fl=1;
        }
        long long ans=0;
        while(res)
        {
            ans=(ans*10+res%10);
            res/=10;
            
        }
        res=ans;
        if(fl)res*=-1;
        if(res>=-(1LL<<31LL)&&res<(1LL<<31LL))return res;
        else return 0;
        
        
    }
};
