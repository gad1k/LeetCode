from unittest import TestCase, main
from tasks.sec_0500.task_0414_third_maximum_number import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertEqual(self.s.thirdMax([3, 2, 1]), 1)

    def test02(self):
        self.assertEqual(self.s.thirdMax([1, 2]), 2)

    def test03(self):
        self.assertEqual(self.s.thirdMax([2, 2, 3, 1]), 1)


if __name__ == '__main__':
    main()
