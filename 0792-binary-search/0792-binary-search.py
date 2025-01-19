class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in set(nums):
            return -1
        if len(nums) == 1:
            return 0
        ndx = len(nums) // 2
        if target == nums[ndx]:
            return ndx
        elif target < nums[ndx]:
            return self.search(nums[0:ndx], target)
        elif target > nums[ndx]:
            return ndx+ 1 + self.search(nums[ndx+1: len(nums)], target)


