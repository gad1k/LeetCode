from unittest import TestCase, main
from tasks.sec_1000.task_0941_valid_montain_array import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertFalse(self.s.validMountainArray([2, 1]))

    def test02(self):
        self.assertFalse(self.s.validMountainArray([3, 5, 5]))

    def test03(self):
        self.assertTrue(self.s.validMountainArray([0, 3, 2, 1]))

    def test04(self):
        self.assertFalse(self.s.validMountainArray([2]))

    def test05(self):
        self.assertFalse(self.s.validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test06(self):
        self.assertFalse(self.s.validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))


if __name__ == '__main__':
    main()
