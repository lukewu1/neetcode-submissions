class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            while stack and h < stack[-1][0]:
                height, index, _ = stack.pop()
                area = height * (i - index)
                maxArea = max(maxArea, area)
            
            if not stack:
                stack.append((h, 0, i))
            else:
                stack.append((h, stack[-1][2] + 1, i))
        
        while stack:
            height, index, _ = stack.pop()
            area = height * (len(heights) - index)
            maxArea = max(maxArea, area)

        return maxArea