class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = collections.defaultdict(int)
        seen[0] = 1

        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            total = prefix - k
            if total in seen:
                count += seen[total]
            
            seen[prefix] += 1
        
        return count


