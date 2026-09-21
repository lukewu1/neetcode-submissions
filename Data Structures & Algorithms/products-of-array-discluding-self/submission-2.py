class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        post = [0 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            pre.append(pre[-1] * nums[i])

        post[len(nums)-1] =  nums[len(nums)-1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i+1] * nums[i]
        
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(post[i+1])
            elif i == (len(nums) - 1):
                output.append(pre[i-1])
            else:
                output.append(pre[i-1] * post[i+1])
        return output
