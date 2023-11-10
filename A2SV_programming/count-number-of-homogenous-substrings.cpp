class Solution {
public:
    long factorial(long n){
        long res = 0;
        while (n){
            res += n;
            n--;
        }
        return res;
    } 
    int countHomogenous(string s) {
        int l = 0;
        int r = 0;
        long ans = 0;
        long mod = 1e9 + 7;
        while (r < s.length()){
            if (s[l] == s[r]){
                r ++;
            }
            else{
             
                ans += factorial(r-l);
                l = r;
            }
        }
       
        ans += factorial(r-l);
        return ans % mod;
    }
};