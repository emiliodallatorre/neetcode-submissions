class Solution:
    def operate(self, b, a, op: str) -> int:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return math.trunc(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        opstack: list[int] = []

        for token in tokens:
            if token in ["-", "+", "*", "/"]:
                opstack.append(self.operate(opstack.pop(), opstack.pop(), token))
            else:
                opstack.append(int(token))

        return opstack[0]