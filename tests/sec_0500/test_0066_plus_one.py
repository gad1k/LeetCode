from unittest import TestCase, main
from tasks.sec_0500.task_0066_plus_one import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.plusOne([1, 2, 3])
        self.assertEqual([1, 2, 4], r)

    def test02(self):
        r = self.s.plusOne([4, 3, 2, 1])
        self.assertListEqual([4, 3, 2, 2], r)

    def test03(self):
        r = self.s.plusOne([9])
        self.assertListEqual([1, 0], r)


if __name__ == '__main__':
    main()
