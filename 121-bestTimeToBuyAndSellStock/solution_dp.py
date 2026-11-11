class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """DP method (kinda)

        Idea is to have "recurrence", where we continue "building" on the state as we move through the array

        Time complexity: O(n)
        Space complexity: O(1)

        """
        max_profit = 0
        min_buy = prices[0]

        for sell in prices:
            max_profit = max(max_profit, sell - min_buy)
            min_buy = min(min_buy, sell)

        return max_profit
