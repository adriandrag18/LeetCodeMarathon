// title: Two Sum
// timestamp: 2024-02-21 20:27:23
// problemUrl: https://leetcode.com/problems/two-sum/
// memory: 13.4 MB
// runtime: 0 ms

#include <bits/stdc++.h>

struct element{
 int val, pos;
};

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      vector<element> elements(nums.size());
      for(int i = 0; i < nums.size(); i++) {
        elements[i].val = nums[i];
        elements[i].pos = i;
      }
      
      std::sort(elements.begin(), elements.end(), [](element a, element b) {return a.val < b.val;});
      vector<int> res;
      int j = nums.size()-1;
      for (int i = 0; i <= j; ) {
        if (elements[i].val + elements[j].val == target) {
          res.push_back(elements[i].pos);
          res.push_back(elements[j].pos);
          break;
        } else if (elements[i].val + elements[j].val < target){
          i++;
        } else {
          j--;
        }
      }
      return res;
    }
};