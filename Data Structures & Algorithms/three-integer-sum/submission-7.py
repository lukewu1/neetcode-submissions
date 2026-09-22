class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        output = []
        for i in range(len(nums)):
            if nums[i] not in seen:
                target = -(nums[i])
                seen.add(nums[i])
                l = i + 1
                r = (len(nums) - 1)
                while l < r:
                    twosum = nums[r] + nums[l]
                    if twosum == target:
                        if [nums[l], nums[r], nums[i]] not in output:
                            output.append([nums[l], nums[r], nums[i]])
                        l += 1
                        r -= 1
                    elif twosum < target:
                        l += 1
                    elif twosum > target:
                        r -= 1
                    
                        
        return output
