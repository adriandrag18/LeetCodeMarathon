// title: Find the Town Judge
// timestamp: 2024-02-22 07:32:27
// problemUrl: https://leetcode.com/problems/find-the-town-judge/
// memory: 121.9 MB
// runtime: 149 ms

class Solution {
public:
  int findJudge(int n, vector<vector<int>>& trust) {
    vector<vector<int>> v(n, vector<int>(n, 0));
    for (int i = 0; i < trust.size(); i++) {
      v[trust[i][0]-1][trust[i][1]-1] = 1;
    }
    for (int i = 0; i < n; i++) {
      int sum = 0;
      for (int j = 0; j < n; j++) {
        sum += v[j][i];
      }
      if (sum == n-1) {
        sum = 0;
        for (int j = 0; j < n; j++) {
          sum += v[i][j];
        }
        if (sum == 0) {
          return i+1;
        }
      }
    }
    return -1;
  }
};