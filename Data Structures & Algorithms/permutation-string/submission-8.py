class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = [0] * 26
        have = [0] * 26

        for c in s1:
            need[ord(c) - 97] += 1
        
        length = len(s1)

        for i, c in enumerate(s2):
            if i > (length - 1):
                have[ord(s2[i - length]) - 97] -= 1
                
            have[ord(c) - 97] += 1
            
            if need == have:
                return True
        
        return False
