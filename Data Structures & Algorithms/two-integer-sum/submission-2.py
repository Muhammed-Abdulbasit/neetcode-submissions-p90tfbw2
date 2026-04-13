class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, n in enumerate(nums):
            soln = target - n
            if soln in prev:
                return [prev[soln], i]
            prev[n] = i