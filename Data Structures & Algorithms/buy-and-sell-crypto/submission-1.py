class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = {}
        maxprof = 0
        maxq = 0 
        bestPriceToBuy = prices[0]
        for i in range(1, len(prices)):
            print("iteration " + str(i))
            if prices[i] < bestPriceToBuy:
                bestPriceToBuy = prices[i]
            maxq = prices[i] - bestPriceToBuy
            if maxq > maxprof:
                maxprof = maxq
        return maxprof