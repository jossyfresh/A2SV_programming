class Solution {
public:
    int subarrayGCD(vector<int>& nums, int k) {
        int ans = 0;
        for (int i = 0 ; i  < nums.size();i++){
            int x = nums[i];
            for (int j = i ; j < nums.size();j++){
                x = __gcd(nums[j],x);
                if (x == k) ans++;
            }
        }
        return ans;
    }
};