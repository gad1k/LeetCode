from unittest import TestCase, main
from tasks.sec_2000.task_1701_average_waiting_time import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.averageWaitingTime([[1, 2], [2, 5], [4, 3]])
        self.assertEqual(5.0, r)

    def test02(self):
        r = self.s.averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]])
        self.assertEqual(3.25, r)


if __name__ == '__main__':
    main()
