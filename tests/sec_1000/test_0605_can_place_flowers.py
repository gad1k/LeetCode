from unittest import TestCase, main
from tasks.sec_1000.task_0605_can_place_flowers import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        r = self.s.canPlaceFlowers([1, 0, 0, 0, 1], 1)
        self.assertTrue(r)

    def test02(self):
        r = self.s.canPlaceFlowers([1, 0, 0, 0, 1], 2)
        self.assertFalse(r)

    def test03(self):
        r = self.s.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2)
        self.assertTrue(r)

    def test04(self):
        r = self.s.canPlaceFlowers([1], 0)
        self.assertTrue(r)


if __name__ == '__main__':
    main()
