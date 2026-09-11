class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = collections.defaultdict(list)
        index = 0
        for i in range(len(nums)):
            seen[nums[i]].append(i)
        
        for i in seen.values():
            if len(i) > 1:
                for j in range(len(i) - 1):
                    print(i[j], i[j+1])
                    if abs(i[j] - i[j+1]) <= k:
                        return True
        return False