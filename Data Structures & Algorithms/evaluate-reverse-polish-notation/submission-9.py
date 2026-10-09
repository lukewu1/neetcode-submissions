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
                    if val2 < 0 and val1 < 0:
                        res = val2//val1
                    elif val2 < 0:
                        res = -(-val2//val1)
                    elif val1 < 0:
                        res = -(-val2//val1)
                    else:
                        res = val2//val1
                    stack.append(res)
        
        return stack[0]