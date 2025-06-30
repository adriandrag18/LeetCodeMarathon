// title: Same Tree
// timestamp: 2024-04-14 19:54:44
// problemUrl: https://leetcode.com/problems/same-tree/
// memory: 11.7 MB
// runtime: 0 ms

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// struct TreeNode {
//       int val;
//       TreeNode *left;
//       TreeNode *right;
//       TreeNode() : val(0), left(nullptr), right(nullptr) {}
//       TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//       TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
// };
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!q && !p)
            return true;

        if (!p || !q) 
            return false;

        if (p->val != q->val)
            return false;

        return isSameTree(p->left, q->left) & isSameTree(p->right, q->right);
    }
};