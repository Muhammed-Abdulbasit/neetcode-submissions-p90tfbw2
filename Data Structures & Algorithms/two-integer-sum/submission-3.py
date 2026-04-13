class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevlist = {}

        for i, n in enumerate(nums):
            soln = target - n
            if soln in prevlist:
                return [prevlist[soln], i]
            prevlist[n] = i