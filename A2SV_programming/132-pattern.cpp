class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        stack<int>st;
        long x = -1e9;
        for (int i = nums.size()-1;i >= 0;i--){
            if (nums[i] < x){
                return true;
            }
            while (st.size() > 0 && st.top() < nums[i]){
                x = st.top();
                st.pop();
            }
            st.push(nums[i]);
        }
        return false;

    }
};