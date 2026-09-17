class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        max_len = 0
        for i in numSet:
            if i-1 not in numSet:
                nxt = i + 1
                while nxt in numSet:
                    nxt += 1
                max_len = max(max_len, nxt - i)

        return max_len