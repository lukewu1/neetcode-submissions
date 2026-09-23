class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_length = 0
        seen = collections.defaultdict(int)
        for r in range(len(nums)):
            seen[nums[r]] += 1
            while seen[0] > k:
                seen[nums[l]] -= 1
                l += 1
            max_length = max(max_length, (r-l+1))
        return max_length