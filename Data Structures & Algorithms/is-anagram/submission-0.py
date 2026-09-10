class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seenS = {}
        seenT = {}

        for i in range(len(s)):
            if s[i] not in seenS:
                seenS[s[i]] = 1
            else:
                seenS[s[i]] += 1

            if t[i] not in seenT:
                seenT[t[i]] = 1
            else:
                seenT[t[i]] += 1
        
        for i in seenS.keys():
            if i not in seenT:
                return False
            if seenS[i] != seenT[i]:
                return False
        
        return True
            
            