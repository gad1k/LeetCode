from unittest import TestCase, main
from tasks.sec_0500.task_0209_minimum_size_subarray_sum import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
        self.assertEqual(2, r)

    def test02(self):
        r = self.s.minSubArrayLen(4, [1, 4, 4])
        self.assertEqual(1, r)

    def test03(self):
        r = self.s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(0, r)


if __name__ == '__main__':
    main()
