class Solution {
public:
    
    double myPow(double x, int n) {
        
        double ans = 1.0;
        bool fl = 0;
        long long n1 = n;
        if ( n < 0 ){
            fl =1;
            n1 *= -1;
        }
        
        while(n1){
            if(n1 % 2 == 1){
                ans = ans * x;
            }
            n1 /= 2;
            x = x * x;
        }
        if ( fl) ans = 1.0 / ans;
        return ans;
        
    }
};