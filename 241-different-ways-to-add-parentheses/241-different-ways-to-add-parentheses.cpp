class Solution {
public:
    bool isDigit(string x) {
        for(auto ch: x) {
            if(ch < '0' || ch > '9')return false;
        }
        return true;
    }
    
    int strToNum(string x) {
        int res = 0;
        for(auto ch: x) {
            res = res * 10 + ch -'0';
        }
        return res;
    }
    
    vector<int> diffWaysToCompute(string expression) {
        if(isDigit(expression)) {
            vector<int> vect{strToNum(expression)};
            return vect;
        }
        
        string kox = expression;
        if(expression[0] == '-') kox = '0'+ expression;
        
        vector<int> ans;
        for(int i = 0; i < kox.size(); i++) {
           
            if(kox[i] == '+' || kox[i] == '-' || kox[i] == '*') {
                string left_s = kox.substr(0, i);
                string right_s = kox.substr(i + 1, (int)kox.size() - i - 1);
                
                cout<<i<<kox[i]<<endl;
                cout<<i<<left_s<<" "<<right_s<<endl;
                
                vector<int> le = diffWaysToCompute(left_s);
                vector<int> ri = diffWaysToCompute(right_s);
                
                
                for(auto x: le) {
                    for(auto y: ri) {
                        if(kox[i] == '+')ans.push_back(x + y);
                        if(kox[i] == '-')ans.push_back(x - y);
                        if(kox[i] == '*')ans.push_back(x * y);
                    }
                }
            }
        }
        return ans;
    }
};