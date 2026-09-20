class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = set()
        seen = set(nums1)
        for i in nums2:
            if i in seen:
                output.add(i)

        return list(output)