from unittest import TestCase, main
from tasks.sec_0500.task_0122_best_time_to_buy_sell_stock_2 import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(7, self.s.maxProfit(prices))

    def test02(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(4, self.s.maxProfit(prices))

    def test03(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(0, self.s.maxProfit(prices))


if __name__ == '__main__':
    main()
