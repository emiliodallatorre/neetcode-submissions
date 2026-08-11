class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc: dict = {}
        st: dict = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if not s[i] in sc:
                sc[s[i]] = 0
            sc[s[i]] += 1

            if not t[i] in st:
                st[t[i]] = 0
            st[t[i]] += 1

        return st == sc