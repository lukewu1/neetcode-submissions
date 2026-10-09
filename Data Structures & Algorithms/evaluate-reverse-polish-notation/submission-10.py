class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def isInteger(val_str):
            try:
                int(val_str)
                return True
            except ValueError:
                return False

        stack = []
        for t in tokens:
            if isInteger(t):
                stack.append(int(t))
            else:
                val1, val2 = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(val1 + val2)
                elif t == '-':
                    stack.append(val2 - val1)
                elif t == '*':
                    stack.append(val1 * val2)
                else:
                    stack.append(int(val2/val1))
        
        return stack[0]