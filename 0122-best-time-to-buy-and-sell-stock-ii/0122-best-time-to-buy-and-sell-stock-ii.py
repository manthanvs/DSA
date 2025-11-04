class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Almost similar like previous question we just need to ensure that we take care of the next terms as well.

        profit = 0

        # Starting the loop from 1 because the following loop would be used to check all the previous values and compare them as well. Since, zero'th index doesn't have any previous values we proceed with first index.
        for i in range(1, len(prices)):
            # If the next day price is great than current day, then obviously we would buy.
            if prices[i] > prices[i - 1]:
                # profit = profit + (prices[i] - prices[i-1])
                profit += prices[i] - prices[i - 1]

            # else if the stock is in decreasing order then the there won't be any profit, and profit would remain zero as it is.
        return profit
