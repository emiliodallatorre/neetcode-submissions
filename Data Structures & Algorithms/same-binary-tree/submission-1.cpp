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

class Solution {
    bool dfsCompare(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true;
        if (!(p && q)) return false;
        if (p->val != q->val) return false;

        // Both exists, with same value if we arrived here
        bool left = true;
        bool right = true;
        if (p->left || q->left) left = dfsCompare(p->left, q->left);
        if (p->right || q->right) right = dfsCompare(p->right, q->right);

        return left && right;
    }

public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return dfsCompare(p, q);
    }
};
