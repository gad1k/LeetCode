from unittest import TestCase, main
from tasks.sec_1500.task_1051_height_checker import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertEqual(self.s.heightChecker([1, 1, 4, 2, 1, 3]), 3)

    def test02(self):
        self.assertEqual(self.s.heightChecker([5, 1, 2, 3, 4]), 5)

    def test03(self):
        self.assertEqual(self.s.heightChecker([1, 2, 3, 4, 5]), 0)


if __name__ == '__main__':
    main()
