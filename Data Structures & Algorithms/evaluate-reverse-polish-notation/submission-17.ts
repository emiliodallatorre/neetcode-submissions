class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    operate(a: number, b: number, op: string): number {
        if (op === "+") {
            return a + b
        } else if (op === "*") {
            return a * b
        } else if (op === "/") {
            return Math.trunc(a / b)
        } else if (op === "-") {
            return a - b
        }
    }

    evalRPN(tokens: string[]): number {
        const ops: string[] = ["+", "-", "*", "/"]

        const stack: number[] = []

        for (const token of tokens) {
            if (ops.includes(token)) {
                const b: number = stack.pop()
                const a: number = stack.pop()

                const c: number = this.operate(a, b, token)

                stack.push(c)
            } else {
                stack.push(Number(token))
            }
        }

        return stack.pop();
    }
}
