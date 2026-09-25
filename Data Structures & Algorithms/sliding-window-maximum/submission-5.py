class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        l = 0
        output = []
        for r in range(len(nums)):
            if r - k == l:
                l += 1
                for i in range(l, r):
                    if nums[i] > nums[l]:
                        l = i
            if nums[r] >= nums[l]:
                l = r
            if r >= (k - 1):
                output.append(nums[l])
        
        return output