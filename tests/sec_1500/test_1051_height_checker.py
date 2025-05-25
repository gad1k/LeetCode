from unittest import TestCase, main
from tasks.sec_1500.task_1051_height_checker import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.heightChecker([1, 1, 4, 2, 1, 3])
        self.assertEqual(3, r)

    def test02(self):
        r = self.s.heightChecker([5, 1, 2, 3, 4])
        self.assertEqual(5, r)

    def test03(self):
        r = self.s.heightChecker([1, 2, 3, 4, 5])
        self.assertEqual(0, r)


if __name__ == '__main__':
    main()
