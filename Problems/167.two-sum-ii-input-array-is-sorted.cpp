// title: Two Sum II - Input Array Is Sorted
// timestamp: 2024-02-21 20:30:27
// problemUrl: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// memory: 18.4 MB
// runtime: 7 ms

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
      sort(numbers.begin(), numbers.end());
      vector<int> res;
      int j = numbers.size()-1;
      for (int i = 0; i <= j; ) {
        if (numbers[i] + numbers[j] == target) {
          res.push_back(i + 1);
          res.push_back(j + 1);
          break;
        } else if (numbers[i] + numbers[j] < target){
          i++;
        } else {
          j--;
        }
      }
      return res; 
    }
};