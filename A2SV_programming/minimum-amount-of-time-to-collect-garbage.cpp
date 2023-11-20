class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        int g = 0;
        int fg = 0;
        int fm = 0;
        int fp = 0;
        int m = 0;
        int p = 0;
        int tr = 0;
       for (int i = 0;i < garbage.size();i++){
           if (garbage[i].find('G') != std::string::npos){
               fg = tr;
           }
           if (garbage[i].find('M') != std::string::npos){
               fm = tr;
           }
           if (garbage[i].find('P') != std::string::npos){
               fp = tr;
           }
          for (int j = 0;j < garbage[i].length() ; j++){
              if (garbage[i][j] == 'G'){
                  g ++;
              }
              if (garbage[i][j] == 'M'){
                  m ++;
              }
              if (garbage[i][j] == 'P'){
                  p ++;
              }
          }
          if (i < travel.size()){
          tr += travel[i];
          }
       } 
       return p + g + m + fm + fg + fp;
    }
};