from unittest import TestCase, main
from tasks.sec_0500.task_0136_single_number import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [2, 2, 1]
        self.assertEqual(self.s.singleNumber(nums), 1)

    def test02(self):
        nums = [4, 1, 2, 1, 2]
        self.assertEqual(self.s.singleNumber(nums), 4)

    def test03(self):
        nums = [1]
        self.assertEqual(self.s.singleNumber(nums), 1)


if __name__ == '__main__':
    main()
