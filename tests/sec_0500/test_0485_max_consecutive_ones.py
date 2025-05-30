from unittest import TestCase, main
from tasks.sec_0500.task_0485_max_consecutive_ones import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
        self.assertEqual(3, r)

    def test02(self):
        r = self.s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])
        self.assertEqual(2, r)


if __name__ == '__main__':
    main()
