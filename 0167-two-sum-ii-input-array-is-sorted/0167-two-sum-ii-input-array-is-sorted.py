class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range (0, len(numbers)):
            diff = target - numbers[i]
            if diff in numbers:
                return [i+1, numbers.index(diff, i+1)+1]