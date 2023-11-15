class Solution {
public:
    int dp(int i,bool buy,vector<int> &prices,vector<vector<vector<int>>> &memo, int count){
        if (i == prices.size()){
            return 0;
        }
        if (count >= 2){
            return 0;
        }
        if (memo[i][buy][count] != -1){
            return memo[i][buy][count];
        }
        
        if (buy) {
            return memo[i][buy][count] = max(dp(i+1,!buy,prices,memo,count)- prices[i],dp(i+1,buy,prices,memo,count)); 
        }
        else{
            return memo[i][buy][count] = max(dp(i+1,!buy,prices,memo,count+1) + prices[i],dp(i+1,buy,prices,memo,count));
        }
    }
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        vector<vector<vector<int>>>memo(n,vector<vector<int>>(2,vector<int>(3,-1)));
        return dp(0,1,prices,memo,0);
        
    }
};