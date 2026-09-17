class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            left = s[l].isalnum()
            right = s[r].isalnum()
            if left and right:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
                    continue
            elif not left:
                l += 1
            elif not right:
                r -= 1

        return True