class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 1:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2] + nums[(len(nums)//2) - 1])/2
        # if not nums1:
        #     if len(nums2) % 2 == 1:
        #         return nums2[len(nums2)//2]
        #     else:
        #         return (nums2[len(nums2)//2] + nums2[(len(nums2)//2) - 1])/2
        # if not nums2:
        #     if len(nums1) % 2 == 1:
        #         return nums1[len(nums1)//2]
        #     else:
        #         return (nums1[len(nums1)//2] + nums1[(len(nums1)//2) - 1])/2

        # totalLength = len(nums1) + len(nums2)
        # pointer1 = 0
        # pointer2 = 0

        # if totalLength % 2 == 1:
        #     while pointer1 + pointer2 != totalLength//2:
        #         if nums1[pointer1] <= nums2[pointer2]:
        #             pointer1 += 1
        #         else:
        #             pointer2 += 1
            
        #     return(min(nums1[pointer1], nums2[pointer2]))
        # else:
        #     while (pointer1 + pointer2 + 1) != totalLength//2:
        #         if nums1[pointer1] <= nums2[pointer2]:
        #             pointer1 += 1
        #         else:
        #             pointer2 += 1
        #     return (nums1[pointer1] + nums2[pointer2])/2

            
            