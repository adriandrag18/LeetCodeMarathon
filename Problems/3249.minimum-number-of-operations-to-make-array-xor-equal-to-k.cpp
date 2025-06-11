// title: Minimum Number of Operations to Make Array XOR Equal to K
// timestamp: 2024-04-29 13:49:44
// problemUrl: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/
// memory: 91.3 MB
// runtime: 104 ms

class Solution {
public:
    int minOperations(vector<int>& nums, int a) {
        int k = a;
        for (auto x: nums)
            k ^= x;

        int res = 0;
        while(k > 0){
            if (k & 1)
                res++;
            k >>= 1;
        }
        return res;
    }
};