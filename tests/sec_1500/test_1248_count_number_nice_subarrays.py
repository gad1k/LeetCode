from unittest import TestCase, main
from tasks.sec_1500.task_1248_count_number_nice_subarrays import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        nums = [1, 1, 2, 1, 1]
        r = self.s.numberOfSubarrays(nums, 3)
        self.assertEqual(2, r)

    def test02(self):
        nums = [2, 4, 6]
        r = self.s.numberOfSubarrays(nums, 1)
        self.assertEqual(0, r)

    def test03(self):
        nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
        r = self.s.numberOfSubarrays(nums, 2)
        self.assertEqual(16, r)


if __name__ == '__main__':
    main()
