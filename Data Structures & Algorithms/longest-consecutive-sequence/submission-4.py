class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNumbers = set(nums)
        seen = set()
        res = 0
        for num in setOfNumbers:
            if num not in seen:
                seen.add(num)
                count = 1
                nextNum = num + 1
                while nextNum in setOfNumbers:
                    seen.add(nextNum)
                    count += 1
                    nextNum += 1

            res = max(res, count)

        return res