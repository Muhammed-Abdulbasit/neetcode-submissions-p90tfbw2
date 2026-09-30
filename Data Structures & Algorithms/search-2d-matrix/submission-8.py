class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check first element of each row starting from bottom
        # if target is smaller, go to next row and binary search
        # if its larger check that row
        # return false
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid = (top+bot)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                row_to_check = mid
                break
        
        if top > bot:
            return False

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l+r)//2
            if target < matrix[row_to_check][mid]:
                r = mid - 1
            elif target > matrix[row_to_check][mid]:
                l = mid + 1
            else:
                return True
        return False