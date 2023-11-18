class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_map<char,int>start;
        unordered_map<char,int>end;
        for (int i = 0; i< s.length();i++){
            if (start.find(s[i]) == start.end()){
                start[s[i]] = i;
                end[s[i]] = i;
            }
            else{
                end[s[i]] = i;
            }
        }
        int ans = 0;
        for (auto &[let,c] : start){
            int st = c;
            int en = end[let];
            set<int>letters;
            for (int i = st+1;i < en;i++){
                letters.insert(s[i]);
            }
        ans += letters.size();
        }
        return ans;

    }
};