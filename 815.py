class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        unordered_map<int,vector<int>>adjlist;
        for (int i = 0; i < routes.size();i++){
            for (auto &node : routes[i]){
                adjlist[node].push_back(i);
            }
        }
        if (target == source){
            return 0;
        }
        queue<int>queue;
        set<int>visited;
        for (auto stops : adjlist[source]){
            queue.push(stops);
            visited.insert(stops);
        }
        int level = 0;
        while (queue.size() > 0){
            int n = queue.size();
            while (n > 0){
                n--;
                int cur = queue.front();
                queue.pop();
                visited.insert(cur);
                for (auto stop: routes[cur]){
                if (stop == target){
                    return level+1;
                }
                for (auto &node : adjlist[stop]){
                    if (visited.find(node) == visited.end()){
                    queue.push(node);
                    visited.insert(node);
                    }
                }
            }
            }
            level++;
        }
        return -1;
    }
    
};