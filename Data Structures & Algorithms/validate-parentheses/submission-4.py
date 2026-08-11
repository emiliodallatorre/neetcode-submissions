class Solution:
    def isValid(self, s: str) -> bool:
        couplings: dict = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        stack: list[str] = []

        for par in s:
            if par in couplings.keys():
                stack.append(par)
            else:
                if stack and par != couplings[stack[-1]]:
                    return False
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
        
        return not stack