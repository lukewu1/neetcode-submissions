class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        max_len = 0
        for i in numSet:
            if i-1 not in numSet:
                start = i
                nxt = start + 1
                while nxt in numSet:
                    nxt += 1
                max_len = max(max_len, nxt - start)

        return max_len