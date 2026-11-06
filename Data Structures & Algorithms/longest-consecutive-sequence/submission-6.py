class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNumbers = set(nums)
        res = 0
        for num in setOfNumbers:
            if num - 1 not in setOfNumbers:
                nextNum = num + 1
                count = 1
                while nextNum in setOfNumbers:
                    nextNum += 1
                    count += 1
                res = max(res, count)

        return res