from unittest import TestCase, main
from tasks.sec_2000.task_1679_max_number_k_sum_pairs import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.maxOperations([1, 2, 3, 4], 5)
        self.assertEqual(2, r)

    def test02(self):
        r = self.s.maxOperations([3, 1, 3, 4, 3], 6)
        self.assertEqual(1, r)

    def test03(self):
        r = self.s.maxOperations([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3)
        self.assertEqual(4, r)


if __name__ == '__main__':
    main()
