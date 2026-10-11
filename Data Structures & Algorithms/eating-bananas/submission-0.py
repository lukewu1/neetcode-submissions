class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minEatingPace = float('inf')
        while l <= r:
            eatingPace = (l + r)//2
            time = 0
            for p in piles:
                time += -(-p//eatingPace)
                if time > h:
                    break
            
            if time <= h:
                r = eatingPace - 1
                minEatingPace = min(minEatingPace, eatingPace)
            else:
                l = eatingPace + 1
        
        return minEatingPace