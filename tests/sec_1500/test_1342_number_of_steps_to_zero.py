from unittest import TestCase, main
from tasks.sec_1500.task_1342_number_of_steps_to_zero import Solution


class TestSolution(TestCase):
    s = Solution()

    def test01(self):
        self.assertEqual(self.s.numberOfSteps(14), 6)

    def test02(self):
        self.assertEqual(self.s.numberOfSteps(8), 4)

    def test03(self):
        self.assertEqual(self.s.numberOfSteps(123), 12)


if __name__ == '__main__':
    main()
