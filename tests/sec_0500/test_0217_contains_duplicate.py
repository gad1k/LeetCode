from unittest import TestCase, main
from tasks.sec_0500.task_0217_contains_duplicate import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(self.s.containsDuplicates(nums))

    def test02(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(self.s.containsDuplicates(nums))

    def test03(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(self.s.containsDuplicates(nums))


if __name__ == '__main__':
    main()
