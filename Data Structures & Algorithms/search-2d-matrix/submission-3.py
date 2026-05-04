class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check first element of each row starting from bottom
        # if target is smaller, go to next row and binary search
        # if its larger check that row
        # return false

        l, r = 0, len(matrix[0]) - 1
        row_to_check = -1

        for i in range(len(matrix) -1, -1, -1):
            first_elem = matrix[i][0]
            if first_elem == target:
                return True
            elif first_elem > target:
                continue
            elif first_elem < target:
                row_to_check = i
                break

        while l <= r:
            mid = (r+l)//2
            curr_num = matrix[row_to_check][mid]
            if curr_num == target:
                return True
            elif curr_num > target:
                r = mid - 1
            else:
                l = mid + 1
        return False