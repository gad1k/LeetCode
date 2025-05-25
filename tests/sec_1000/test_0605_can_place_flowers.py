from unittest import TestCase, main
from tasks.sec_1000.task_0605_can_place_flowers import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        result = self.s.canPlaceFlowers([1, 0, 0, 0, 1], 1)
        self.assertTrue(result)

    def test02(self):
        result = self.s.canPlaceFlowers([1, 0, 0, 0, 1], 2)
        self.assertFalse(result)

    def test03(self):
        result = self.s.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2)
        self.assertTrue(result)

    def test04(self):
        result = self.s.canPlaceFlowers([1], 0)
        self.assertTrue(result)


if __name__ == '__main__':
    main()
