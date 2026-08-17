class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return all([s[i] == s[-i - 1] for i in range(len(s) // 2)])