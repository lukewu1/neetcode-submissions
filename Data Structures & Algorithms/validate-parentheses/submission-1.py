class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for bracket in s:
            if bracket in opening.values():
                stack.append(bracket)
            else:
                if not stack:
                    return False
                else:
                    bracketPopped = stack.pop()
                    if opening[bracket] != bracketPopped:
                        return False
        
        if stack:
            return False
        return True