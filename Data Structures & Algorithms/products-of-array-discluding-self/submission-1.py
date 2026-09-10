class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        seen = collections.defaultdict(list)
        total = 1
        for i in range(len(nums)):
            seen[nums[i]].append(i)
            if nums[i] != 0:
                total = total * nums[i]

        if 0 not in seen:
            for i in range(len(nums)):
                nums[i] = int(total/nums[i])
        elif len(seen[0]) == 1:
            for i in range(len(nums)):
                if i == seen[0][0]:
                    nums[i] = total
                else:
                    nums[i] = 0
        else:
            for i in range(len(nums)):
                nums[i] = 0
        return nums
    
