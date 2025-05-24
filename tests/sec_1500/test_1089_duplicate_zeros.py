from unittest import TestCase, main
from tasks.sec_1500.task_1089_duplicate_zeros import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        arr = [1, 0, 2, 3, 0, 4, 5, 0]
        self.s.duplicateZeros(arr)
        self.assertListEqual(arr, [1, 0, 0, 2, 3, 0, 0, 4])

    def test02(self):
        arr = [1, 2, 3]
        self.s.duplicateZeros(arr)
        self.assertListEqual(arr, [1, 2, 3])


if __name__ == '__main__':
    main()
