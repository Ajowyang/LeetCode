class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortnums = sorted(nums)
        result = []
        for i in range(0, len(sortnums)):
            if i > 0 and (sortnums[i] == sortnums[i-1]):
                continue
            left = i + 1
            right = len(sortnums) - 1
            while left < right:
                threesum = sortnums[i] + sortnums[left] + sortnums[right]
                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    result.append([sortnums[i], sortnums[left], sortnums[right]])
                    left += 1
                    while (sortnums[left] == sortnums[left-1]) and (left < right):
                        left +=1
        return result