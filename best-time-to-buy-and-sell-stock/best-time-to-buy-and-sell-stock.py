class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 1
        l=0
        maxProfit=0
        
        while (r < len(prices)):
            if (prices[l]< prices[r]):
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit , profit)
                print(maxProfit)
            else:
                l = r
            r+=1
        return maxProfit
        
        
        # index = 0
        # profit= 0
        # for i in range(len(prices)):
        #     difference  = prices[i] - prices[index]
        #     if difference < 0:
        #         index = i
        #     elif difference > profit and difference >0:
        #         profit = difference
        # return profit