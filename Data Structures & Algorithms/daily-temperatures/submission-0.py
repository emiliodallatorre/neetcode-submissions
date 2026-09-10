class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: list[int] = []
        result: list[int] = [0 for t in temperatures]

        for i, t in enumerate(temperatures):
            if not stack:
                stack.append(i)
                continue
            
            # We now know that we need to close stuff in the stack
            for u in reversed(stack):
                if temperatures[u] >= t:
                    break

                result[u] = i - u
                stack.pop()
            
            stack.append(i)

        return result
            
