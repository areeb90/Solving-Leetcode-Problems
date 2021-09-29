class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index = 0
        profit= 0
        for i in range(len(prices)):
            difference  = prices[i] - prices[index]
            if difference < 0:
                index = i
            elif difference > profit and difference >0:
                profit = difference
        return profit