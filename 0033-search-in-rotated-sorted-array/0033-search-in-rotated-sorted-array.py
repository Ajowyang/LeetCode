class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        

        while left <= right:
            if (right - left) == 1:
                if nums[right] == target:
                    return right
                elif nums[left] == target:
                    return left
                else:
                    return -1
                
            mid = (left + right) // 2
            print(f'{nums[left:right+1]}, mid:{mid}')
            if nums[mid] == target:
                return mid

            #nums[mid] in right sorted section
            if nums[right] >= nums[mid]:
                print('nums[mid] in right sorted')
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                    #target in left portion
                elif target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                    #target in right portion

            #nums[mid] in left sorted
            elif nums[left] < nums[mid]:
                print(f'nums[mid] in left sorted, target:{target}')
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                    #target in left portion
                elif target > nums[mid] or target < nums[left]:
                    left = mid + 1
                    #target in right portion
        return -1