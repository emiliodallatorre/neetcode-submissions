class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        set<int> content;

        cout << "Checking rows..." << endl;
        for (auto& row : board) {
            for (auto& el : row) {
                if (el == '.') continue;
                
                if (content.count(el - '0')) {
                    return false;
                }

                content.insert(el - '0');
            }

            content.clear();
        }

        cout << "Checking cols..." << endl;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char el = board[j][i];

                if (el == '.') continue;

                if (content.count(el - '0')) {
                    return false;
                }

                content.insert(el - '0');
            }

            content.clear();
        }

        cout << "Checking blocks..." << endl;
        for (int block = 0; block < 9; block++) {
            int blockOffsetX = (block % 3) * 3;
            int blockOffsetY = ((int) block / 3) * 3;

            for (int x = 0; x < 3; x++) {
                for (int y = 0; y < 3; y++) {
                    char el = board[x+blockOffsetX][y+blockOffsetY];

                    if (el == '.') continue;

                    if (content.count(el - '0')) {
                        return false;
                    }

                    content.insert(el - '0');
                }
            }

            content.clear();
        }

        return true;
    }
};
