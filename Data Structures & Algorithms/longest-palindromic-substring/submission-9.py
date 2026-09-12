class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        longest_global: str = ""

        def check(i: int, j: int, s: str) -> str:
            longest_local: str = ""
            while j < len(s) and i >= 0 and s[i] == s[j]:
                longest_local = s[i:j+1]

                i -= 1
                j += 1
            
            return longest_local

        for i in range(len(s) - 1):
            longest_local_odd: str = check(i, i, s)
            if len(s) > 1:
                longest_local_even: str = check(i, i+1, s)
            
            if len(longest_local_odd) > len(longest_local_even):
                longest_local = longest_local_odd
            else:
                longest_local = longest_local_even
            
            if len(longest_local) > len(longest_global):
                longest_global = longest_local
        
        return longest_global