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
private:
    int longest = 0;

    int computeDiameterRecursively(TreeNode* root) {
        if (!root->left && !root->right) {
            return 1;
        }

        int left = 0;
        int right = 0;

        if (root->left) left = computeDiameterRecursively(root->left);
        if (root->right) right = computeDiameterRecursively(root->right);

        int diameter = max(left, right);
        longest = max(longest, left + right);

        return diameter + 1;
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        int maxLength = -1;

        computeDiameterRecursively(root);

        return longest;
    }
};
