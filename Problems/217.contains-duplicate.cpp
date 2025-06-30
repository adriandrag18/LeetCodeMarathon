// title: Contains Duplicate
// timestamp: 2024-10-31 14:56:54
// problemUrl: https://leetcode.com/problems/contains-duplicate/
// memory: 61.2 MB
// runtime: 24 ms

// #include <algorithm>

// using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 1; i < nums.size(); i++)
            if (nums[i-1] == nums[i])
                return true;
        return false;
    }
};