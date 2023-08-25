class Solution:
    def maxProfit(self, prices) -> int:
        #First check if the array is empy (constraint shows 0 <= prices[i] is possible)
        if not prices:
            return 0

        # Initialise empy variables to loop
        lowest_price = prices[0]
        max_profit = 0

        for price in prices:
            # update the lowest price variable if a smaller price is found
            lowest_price = min(lowest_price, price)

            # calculate each potential profit
            current_profit = price - lowest_price
            
            # update the maximum profit
            max_profit = max(max_profit, current_profit)
        
        return max_profit