class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int ans = 0;
        int l = 0;
        int r = nums.size()-1;
        sort(nums.begin(),nums.end());
        while (l < r){
            if (nums[l] + nums[r] > k){
                r--;
            }
            else if(nums[l] + nums[r] < k){
                l ++;
            }
            else{
                ans++;
                l++;
                r--;
            }
        }
        return ans;
    }
};