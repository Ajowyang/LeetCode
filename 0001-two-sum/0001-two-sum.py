class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1: len(nums)]:
                return [i, nums[i+1:len(nums)].index(diff)+i+1]
        