// title: Product of Array Except Self
// timestamp: 2024-11-01 11:53:44
// problemUrl: https://leetcode.com/problems/product-of-array-except-self/
// memory: 40.3 MB
// runtime: 2 ms

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size()), r(nums.size(), 1), l(nums.size(), 1);
        for (int i = 1; i < nums.size(); i++)
            l[i] = l[i - 1] * nums[i - 1];
        for (int i = nums.size() - 2; i >= 0; i--)
            r[i] = r[i + 1] * nums[i + 1];
        for (int i = 0; i < nums.size(); i++)
            res[i] = l[i] * r[i];
        
        return res;
    }
};