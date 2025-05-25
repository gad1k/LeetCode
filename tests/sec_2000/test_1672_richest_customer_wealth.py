from unittest import TestCase, main
from tasks.sec_2000.task_1672_richest_customer_wealth import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.maximumWealth([[1, 2, 3], [3, 2, 1]])
        self.assertEqual(6, r)

    def test02(self):
        r = self.s.maximumWealth([[1, 5], [7, 3], [3, 5]])
        self.assertEqual(10, r)

    def test03(self):
        r = self.s.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])
        self.assertEqual(17, r)


if __name__ == '__main__':
    main()
