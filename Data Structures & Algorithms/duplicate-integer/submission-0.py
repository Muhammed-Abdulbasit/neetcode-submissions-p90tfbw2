class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevList = {}

        # go through list of nums
        for i, n in enumerate(nums):
            if nums[i] in prevList:
                return True
            prevList[n] = i
        
        return False