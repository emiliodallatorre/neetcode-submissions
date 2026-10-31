class Solution {
    bool confrontMaps(unordered_map<char, int> s1, unordered_map<char, int> s2) {
        return s1 == s2;
    }

public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) {
            return false;
        }

        int i = 0;
        int j = s1.length() - 1;

        unordered_map<char, int> s2_window;
        unordered_map<char, int> target;

        for (; i <= j; i++) {
            if (!s2_window.contains(s2[i])) s2_window[s2[i]] = 0;
            if (!target.contains(s1[i])) target[s1[i]] = 0;

            s2_window[s2[i]]++;
            target[s1[i]]++;
        }
        i = 0;

        do {
            cout << i << " " << j << endl;
            if(confrontMaps(s2_window, target)) return true;

            s2_window[s2[i]]--;
            if (s2_window[s2[i]] == 0) s2_window.erase(s2[i]);
            i++;

            j++;
            if (!s2_window.contains(s2[j])) s2_window[s2[j]] = 0;
            s2_window[s2[j]]++;
        } while (j < s2.length());

        return false;
    }
};
