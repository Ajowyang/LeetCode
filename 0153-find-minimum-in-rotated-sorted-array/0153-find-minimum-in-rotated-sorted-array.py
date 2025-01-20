class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            midway = (left + right) // 2
            # print(f'left: nums[{left}] = {nums[left]}, midway: nums[{midway}] = {nums[midway]} right: nums[{right}] = {nums[right]}')
            if (right - left) == 1:
                return (nums[left] if nums[left] < nums[right] else nums[right])
            if left == right:
                return nums[left]
            
            if (nums[left] > nums[midway] and nums[right] > nums[midway]) :
                right = midway 
            elif (nums[left] < nums[midway] and nums[right] < nums[midway]):
                left = midway + 1
            elif nums[left] < nums[midway] and nums[right] > nums[midway]:
                right = midway -1