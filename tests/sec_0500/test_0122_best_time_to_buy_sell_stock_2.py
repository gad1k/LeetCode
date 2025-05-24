from unittest import TestCase, main
from tasks.sec_0500.task_0122_best_time_to_buy_sell_stock_2 import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.s.maxProfit(prices), 7)

    def test02(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(self.s.maxProfit(prices), 4)

    def test03(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(self.s.maxProfit(prices), 0)


if __name__ == '__main__':
    main()
