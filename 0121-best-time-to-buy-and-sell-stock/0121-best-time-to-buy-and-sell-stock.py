class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1

        # Would keep a check of the prices where the profit concluded by the prices[sell] - prices[buy] is at maximum.
        maxProfit = 0

        while sell < len(prices):  # As in when the array elements have traversed completely.
            # For a profitable transaction.
            if prices[buy] < prices[sell]:  # a profit basic condition
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)  # Whichever profit is maximum, let it be current ($profit) or previous ($maxProfit) store it in $maxProfit.

            # For a loss transaction.
            else:
                # As the selling price is not greater than the buying price. Therefor the selling price should be the new buying price.
                buy = sell
            
            # Regardless of our conditions the selling prices should be considered to be updated, to check on further days. 
            sell += 1 
        
        return maxProfit