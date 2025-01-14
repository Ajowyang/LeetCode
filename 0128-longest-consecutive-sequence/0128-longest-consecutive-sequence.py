class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1
        num_set = set(nums)

        for num in num_set:
            if (num - 1) not in num_set:
                streak = 1
                check_for = num +1
                while check_for in num_set:
                    streak += 1
                    check_for += 1
                if streak > result:
                    result = streak
       
        return result