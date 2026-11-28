class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        stack = []
        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                match token:
                    case '+':
                        res = num1 + num2
                    case '-':
                        res = num1 - num2
                    case '*':
                        res = num1 * num2
                    case '/':
                        res = int(num1 / num2)
                stack.append(res)
            else: 
                num = int(token)
                stack.append(num)
        return stack.pop()