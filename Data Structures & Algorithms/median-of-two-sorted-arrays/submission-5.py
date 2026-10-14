class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Easiest way to solve, just combine arrays and then find median, WORSE TIME COMPLEXITY
        # nums = nums1 + nums2
        # nums.sort()
        # if len(nums) % 2 == 1:
        #     return nums[len(nums)//2]
        # else:
        #     return (nums[len(nums)//2] + nums[(len(nums)//2) - 1])/2
            
        m, n = len(nums1), len(nums2)
        total = m + n
        i = j = 0
        prev = curr = 0

        for _ in range(total // 2 + 1):
            prev = curr
            # take from A if B is used up, or A's value is smaller
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if total % 2 == 1:
            return float(curr)
        return (prev + curr) / 2
            
            