class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        current_sum = 0
        res = 0
        
        for num in nums:
            current_sum += num
            res += counts[current_sum - goal]
            counts[current_sum] += 1
            
        return res