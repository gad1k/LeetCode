from unittest import TestCase, main
from tasks.sec_1500.task_1342_number_of_steps_to_zero import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertEqual(6, self.s.numberOfSteps(14))

    def test02(self):
        self.assertEqual(4, self.s.numberOfSteps(8))

    def test03(self):
        self.assertEqual(12, self.s.numberOfSteps(123))


if __name__ == '__main__':
    main()
