class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countW = 0
        minCount = 100
        for i in range(len(blocks)):
            if blocks[i] == 'W':
                countW += 1
            if i >= k and blocks[i-k] == 'W':
                countW -= 1
            if i >= k - 1:
                minCount = min(minCount, countW)

        return minCount