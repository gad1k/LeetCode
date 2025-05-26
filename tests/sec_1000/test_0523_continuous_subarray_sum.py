from unittest import TestCase, main
from tasks.sec_1000.task_0523_continuous_subarray_sum import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.checkSubarraySum([23, 2, 4, 6, 7], 6)
        self.assertTrue(r)

    def test02(self):
        r = self.s.checkSubarraySum([23, 2, 6, 4, 7], 6)
        self.assertTrue(r)

    def test03(self):
        r = self.s.checkSubarraySum([23, 2, 6, 4, 7], 13)
        self.assertFalse(r)

    def test04(self):
        r = self.s.checkSubarraySum([23, 2, 4, 6, 6], 7)
        self.assertTrue(r)


if __name__ == '__main__':
    main()
