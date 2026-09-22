class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = 0
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        
        total_area = 0
        while l <= r:
            if left_max <= right_max:
                water_count = min(left_max, right_max) - height[l]
                left_max = max(left_max, height[l])
                l += 1
            else:
                water_count = min(left_max, right_max) - height[r]
                right_max = max(right_max, height[r])
                r -= 1
            
            if water_count > 0:
                total_area += water_count
    
        return total_area
                

            
            