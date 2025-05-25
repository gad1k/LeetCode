from unittest import TestCase, main
from tasks.sec_1000.task_0941_valid_montain_array import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.validMountainArray([2, 1])
        self.assertFalse(r)

    def test02(self):
        r = self.s.validMountainArray([3, 5, 5])
        self.assertFalse(r)

    def test03(self):
        r = self.s.validMountainArray([0, 3, 2, 1])
        self.assertTrue(r)

    def test04(self):
        r = self.s.validMountainArray([2])
        self.assertFalse(r)

    def test05(self):
        r = self.s.validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertFalse(r)

    def test06(self):
        r = self.s.validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        self.assertFalse(r)


if __name__ == '__main__':
    main()
