# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Инициализация минимальной цены как бесконечность
        max_profit = 0  # Инициализация максимальной прибыли как 0
        for price in prices:  # Цикл по всем ценам
            if price < min_price:  # Если текущая цена меньше минимальной
                min_price = price  # Обновляем минимальную цену покупки
            elif price - min_price > max_profit:  # Если разница больше максимальной прибыли
                max_profit = price - min_price  # Обновляем максимальную прибыль
        return max_profit  # Возвращаем максимальную прибыль



# Примеры использования
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))

