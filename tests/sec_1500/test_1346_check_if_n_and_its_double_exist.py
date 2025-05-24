from unittest import TestCase, main
from tasks.sec_1500.task_1346_check_if_n_and_its_double_exist import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertTrue(self.s.checkIfExist([10, 2, 5, 3]))

    def test02(self):
        self.assertFalse(self.s.checkIfExist([3, 1, 7, 11]))

    def test03(self):
        self.assertTrue(self.s.checkIfExist([7, 1, 14, 11]))


if __name__ == '__main__':
    main()
