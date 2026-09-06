class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed: dict = {}

        for s in strs:
            key: str = "".join(sorted(s))

            if not key in hashed:
                hashed[key] = []

            hashed[key].append(s)

        return list(hashed.values())