class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>mp;
        vector<int>ans(2);
        for (int i = 0 ; i < nums.size();i++){
            int dif = target -  nums[i];
            if (mp.find(dif) != mp.end()){
                ans[0] = mp[dif];
                ans[1] = i;
            }
            mp[nums[i]] = i;
        }
        return ans;
    }
};