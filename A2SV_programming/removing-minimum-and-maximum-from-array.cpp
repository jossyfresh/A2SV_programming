class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int mx = *max_element(nums.begin(),nums.end());
        int mn = *min_element(nums.begin(),nums.end());
        int res = 0;
        int last = 0;
        int n = nums.size();
        bool flag2 = false;
        for (int i = 0 ; i < nums.size();i++){
            if (nums[i] == mx || nums[i] == mn){
                if (flag2){ 
                    res = max(res,i-(last + 1));  
                }
                else {
                    res = max(res,i - (last));    
                }
                flag2 = true;
                last = i;
                
            }
        }
        int las = nums.size()-1;
        bool flag = false;
        for (int i = nums.size()-1;i>=0;i--){
             if (nums[i] == mx || nums[i] == mn){
                if (flag) {
                    res = max(res,las-(i+1));
                }
                else {
                    res = max(res,las - (i));
                }
                flag = true;
                las = i;
                
             }
        }
        return nums.size() - res;

    }
};