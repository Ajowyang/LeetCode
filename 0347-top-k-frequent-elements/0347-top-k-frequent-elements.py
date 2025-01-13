class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        dict = {}
        highest = []
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        print(dict)
        for i in range(0, k):
            highest = 0
            high_freq = 0
            for key, value in dict.items():
                if value > high_freq:
                    highest = key
                    high_freq = value
            print(highest, high_freq)
            result.append(highest)
            dict.pop(highest)

        return result
        