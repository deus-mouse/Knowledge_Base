# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
'''

prices = [7,1,5,3,6,4]  # 7
prices = [1,2,3,4,5]  # 4
prices = [7,6,4,3,1]  # 0


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit








