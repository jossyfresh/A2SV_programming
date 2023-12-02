class Solution {
public:
    void setvalue(vector<int>mat,vector<vector<int>> &ans,int col){
        for (int i = 0 ; i < mat.size();i++){
            ans[i][col] = mat[i];
        }
    }
    void rotate(vector<vector<int>>& matrix) {
        vector<vector<int>>ans(matrix.size(),vector<int>(matrix.size(),0));
        int col = matrix.size()-1;
        for (int i = 0 ; i  < matrix.size();i++){
            setvalue(matrix[i],ans,col);
            col--;
        }
        matrix = ans;
    }
};