class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if len(t) == len(s) and Counter(s) != Counter(t):
            return ""

        seenS = collections.defaultdict(int)
        seenT = Counter(t)
        need = len(seenT)
        have = 0

        l, r = 0, 0
        index = ()
        length = float('inf')
        while r < len(s):
            while r < len(s) and have != need:
                if s[r] in t:
                    seenS[s[r]] += 1
                    if seenS[s[r]] == seenT[s[r]]:
                        have += 1
                r += 1

            while have == need:
                if (r - l) < length:
                    index = (l,r)
                    length = r - l
                if s[l] in t:
                    seenS[s[l]] -= 1
                    if seenS[s[l]] < seenT[s[l]]:
                        have -= 1
                l += 1
        
        if not index:
            return ""
        return s[index[0]:index[1]]



        
