// title: Find Building Where Alice and Bob Can Meet
// timestamp: 2024-12-22 17:26:06
// problemUrl: https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/
// memory: 248.1 MB
// runtime: 51 ms

class Solution {
public:
vector<int> leftmostBuildingQueries(vector<int>& heights, vector<vector<int>>& queries) {
        int n=heights.size(), qz=queries.size();
        vector<int> ans(qz, -1);
        vector<pair<int, int>> idx;

        for (int i= 0; i< qz; i++) {
            int& x=queries[i][0], & y=queries[i][1];
            if (x > y) // let x <= y
                swap(x, y);
            if (x == y|| heights[x]<heights[y])
                ans[i] = y;
            else idx.emplace_back(y, i);
        }

        sort(idx.begin(), idx.end(), greater<>());
        vector<pair<int, int>> stack;

        int j=n-1;
        for (auto [_, i] : idx) {
            int x = queries[i][0];
            int y = queries[i][1];
            for (; j >y; j--) {
                while (!stack.empty() && heights[stack.back().second] < heights[j])
                    stack.pop_back();
                stack.emplace_back(heights[j], j);
            }

            // Check if accessing elements beyond the bounds of stack here
            auto it=upper_bound(stack.rbegin(), stack.rend(), make_pair(heights[x], n));
            ans[i]=(it==stack.rend()) ?-1 : it->second;
        }
        return ans;
    }
};