class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Two pointer method

        Sliding window with 2 pointers (l,r) moving dynamically
        * `r` will constantly shift right as we check if the max profit and that `r` can be higher
        * the moment we find `r < l`, means we have a lower buy-in day, shift `l` to `r`!

        Time complexity: O(n)
        Space complexity: O(1)

        """

        max_profit = 0

        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]

            # better version
            max_profit = max(profit, max_profit)

            # bigger profit, update max_profit tracker
            # if profit > max_profit:
            #     max_profit = profit

            if prices[l] > prices[r]:
                l = r

            r += 1

        return max(max_profit, 0)
