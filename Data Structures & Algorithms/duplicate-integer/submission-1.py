class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # loop through array
        # check if current number exists in hash map
        # if yes, return true
        # if no, add num to hash map
        
        currentnums = []
        for i in range(len(nums)):
            if nums[i] in currentnums:
                return True
            else:
                currentnums.append(nums[i])

        return False