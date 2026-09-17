class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        max_len = 0
        for i in numSet:
            if i-1 not in numSet:
                start = i
                length = 1
                next = start + 1
                while next in numSet:
                    next += 1
                    length += 1
                max_len = max(max_len, length)

        return max_len