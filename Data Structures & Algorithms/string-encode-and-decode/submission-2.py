class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded: str = ""
        header: str = ""

        for s in strs:
            header += f"{len(s)}-"
            encoded += s

        return f"{header}--{encoded}"

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        header: str = s[0:s.index("---")]
        lens: list[int] = map(int, header.split("-"))

        strs: list[str] = []
        cursor: int = 0
        s = s[s.index("---") + 3:]
        for l in lens:
            strs.append(s[:l])
            s = s[l:]

        return strs