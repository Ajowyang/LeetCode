class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range(len(nums)):
            if dict.get(nums[i]) == None:
                dict[nums[i]] = True
            else:
                return True
        return False
        