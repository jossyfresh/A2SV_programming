class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        vector<int>time;
        for (int i = 0; i < dist.size();i++){
            double t = double(dist[i])/double(speed[i]);
            time.push_back(ceil(t));
        }
        sort(time.begin(),time.end());
        int t = 1;
        int ans = 0;
        for (int i = 0 ; i < time.size(); i++){
            if (t > time[i]){
                break;
            }
            ans++;
            t++;
        }
        return ans;
    }
};