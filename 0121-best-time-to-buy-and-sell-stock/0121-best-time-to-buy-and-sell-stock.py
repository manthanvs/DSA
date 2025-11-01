class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initializing two pointers: 'buy' (buying day) and 'sell' (selling day).
        buy, sell = 0, 1

        # maxProfit would be the Variable to store the maximum profit that can be achieved.
        maxProfit = 0

        # Here, the loop runs until the 'sell' pointer reaches the end of the price list. 
        while sell < len(prices):
            
            # Profit condition: We check here, if the current selling price is greater than the buying price i,e. buy < dell — a profitable condition. 
            if prices[buy] < prices[sell]:
                
                # Calculate profit for the current buy-sell pair.
                profit = prices[sell] - prices[buy]
                
                # Update 'maxProfit' with the higher value between current($profti which we calculated just now) and previous profits($maxProft which is stored previously).
                maxProfit = max(maxProfit, profit)
            
            # Loss condition: If the selling price is less than or equal to the buying price — it's a loss or no gain.
            else:
                # We move the 'buy' pointer to the 'sell' pointer position, as the new price could be a better buying opportunity.
                buy = sell
            
            # Move the 'sell' pointer forward to check the next day's price.
            sell += 1
        
        # Returning the highest profit possible, if the sell pointer exceeds then by default it would give 0.
        return maxProfit
