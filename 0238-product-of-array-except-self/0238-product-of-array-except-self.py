class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zero_cnt = 0
        for num in nums:
            if num:
                total_prod *= num
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)
        print(total_prod, zero_cnt)
        result = []
        for num in nums:
            if zero_cnt == 1:
                if num:
                    result.append(0)
                    continue
                else:
                    result.append(total_prod)
                    continue
            result.append(total_prod // num)
        print(result)
        return result
        