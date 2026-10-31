class Solution {
public:
    int characterReplacement(string s, int k) {
        int i = 0;
        int j = 1;

        int maxLength = 0;
        unordered_map<char, int> windowContent;
        windowContent[s[i]] = 0;
        windowContent[s[j]] = 0;
        windowContent[s[i]]++;
        windowContent[s[j]]++;

        while (i < s.length()) {
            // if valid window extend, if not close

            char mostPresentLetter;
            int mostPresentLetterCount = 0;
            int totalLettersInWindow = 0;

            for (auto& element : windowContent) {
                if (mostPresentLetterCount < element.second) {
                    mostPresentLetter = element.first;
                    mostPresentLetterCount = element.second;
                }

                totalLettersInWindow += element.second;
            }

            bool validWindow = totalLettersInWindow - mostPresentLetterCount <= k;
            if (validWindow) {
                if (j - i > maxLength) {
                    maxLength = j - i;
                }
            }

            if (validWindow && j < s.length() - 1) {
                j++;

                if (!windowContent.contains(s[j])) {
                    windowContent[s[j]] = 0;
                }

                windowContent[s[j]]++;
            } else {
                if (j + 1 == s.length() && validWindow) {
                    i = s.length(); // No point in iterating
                } else {
                    windowContent[s[i]]--;

                    i++;
                }
            }

        }

        return maxLength + 1;
    }
};
