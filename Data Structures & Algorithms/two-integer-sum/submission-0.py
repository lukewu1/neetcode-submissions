class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            target_value = target - nums[i]
            if target_value not in seen:
                seen[nums[i]] = i
            else:
                return [seen[target_value], i]