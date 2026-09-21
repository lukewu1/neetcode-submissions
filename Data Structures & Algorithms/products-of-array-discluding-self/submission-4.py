class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1 for _ in range(length)]

        for i in range(1, length):
            output[i] = (output[i-1] * nums[i-1])
    
        suffix = 1
        for i in range(length - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
