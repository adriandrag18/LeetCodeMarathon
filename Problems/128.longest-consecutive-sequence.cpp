// title: Longest Consecutive Sequence
// timestamp: 2024-11-01 12:11:15
// problemUrl: https://leetcode.com/problems/longest-consecutive-sequence/
// memory: 74.7 MB
// runtime: 79 ms

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() < 2)
            return nums.size();
        
        unordered_set<int> s;
        for (auto el: nums)
            s.insert(el);
        
        int m = 1;
        for (auto el: nums) {
            int l = 1;
            if (s.find(el+1) == s.end())
                while (s.find(el-l) != s.end())
                    l++;
            m = max(l, m);
        }
        return m;
    }
};