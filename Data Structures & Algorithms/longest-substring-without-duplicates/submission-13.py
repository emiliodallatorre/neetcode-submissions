
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        longest = 0
        letters = set()

        for j in range(len(s)):
            while s[j] in letters:
                letters.remove(s[i])
                i += 1

            letters.add(s[j])
            longest = max(longest, j - i + 1)

        return longest
