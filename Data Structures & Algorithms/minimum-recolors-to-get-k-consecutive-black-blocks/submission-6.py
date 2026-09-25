class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countW = 0
        minCount = float('inf')
        for i, c in enumerate(blocks):
            if c == 'W':
                countW += 1
            if i >= k and blocks[i - k] == 'W':
                countW -= 1          # drop the element leaving the window
            if i >= k - 1:
                minCount = min(minCount, countW)
        return minCount