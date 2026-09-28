class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketKeys = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for bracket in s:
            if bracket in bracketKeys.values():
                stack.append(bracket)
            else:
                if not stack:
                    return False
                else:
                    bracketPopped = stack.pop()
                    if bracketKeys[bracket] != bracketPopped:
                        return False
        
        if stack:
            return False
        return True