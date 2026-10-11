class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findRow():
            for i in range(len(matrix) - 1):
                if matrix[i][0] <= target < matrix[i+1][0]:
                    return i

            return len(matrix) - 1
        
        index = findRow()
        l, r = 0, len(matrix[index]) - 1
        print(index)
        while l <= r:
            mid = (l + r)//2
            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

