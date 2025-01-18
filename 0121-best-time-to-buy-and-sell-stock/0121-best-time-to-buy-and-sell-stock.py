class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_prof = 0
        while r < (len(prices)):
            prof = prices[r] - prices[l]
            max_prof = max(max_prof, prof)
            if prices[l] > prices[r]:
                l = r
            r += 1
        return max_prof