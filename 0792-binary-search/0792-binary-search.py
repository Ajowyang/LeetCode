class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            midway = (right + left) // 2
            if nums[midway] == target:
                return midway
            elif target < nums[midway]:
                right = midway - 1
            elif target > nums[midway]:
                left = midway + 1
        return -1