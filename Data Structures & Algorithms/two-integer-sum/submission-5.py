class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {} # key : value = index : integer

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev:
                return [prev[diff], i]
            prev[num] = i