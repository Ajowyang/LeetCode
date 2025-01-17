class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        window_start = 0
        for i in range(1, len(prices), 1):
            if prices[i] < prices[window_start]:
                window_start = i
                continue

            if prices[i] - prices[window_start] > result:
                result = (prices[i] - prices[window_start])
               
           
        
        return result
        