class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # loop through array
        # check if current number exists in hash map
        # if yes, return true
        # if no, add num to hash map
        prev = set()

        for i in range(len(nums)):
            if nums[i] in prev:
                return True
            prev.add(nums[i])
        return False

