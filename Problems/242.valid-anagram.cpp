// title: Valid Anagram
// timestamp: 2024-10-31 15:06:20
// problemUrl: https://leetcode.com/problems/valid-anagram/
// memory: 10.1 MB
// runtime: 1 ms

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> freq;
        for (auto &c: s)
            freq[c]--;
        for (auto &c: t)
            freq[c]++;
        for (auto el: freq)
            if (el.second != 0)
                return false;
        return true;
    }
};